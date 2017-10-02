import numpy as np
from sklearn import metrics


def cal_auc(method):
    v_result_1 = np.array([])
    v_result_2 = np.array([])
    for i in range(5):
        tmp_v_result = np.loadtxt("result/bagging_" + method + "/fold_" + str(i + 1) + "_test").astype(float)
        tmp_v_result_1 = tmp_v_result[:197]
        tmp_v_result_2 = tmp_v_result[197:]
        v_result_1 = np.concatenate((v_result_1, tmp_v_result_1))
        v_result_2 = np.concatenate((v_result_2, tmp_v_result_2))
    pred = np.true_divide(np.concatenate((v_result_1, v_result_2)), 200)
    y = np.concatenate((np.zeros(1020) + 1, np.zeros(204000)), axis=0)
    fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=1)
    print metrics.auc(fpr, tpr)


def cal_validation_result_by_mean(method, size):
    auc = np.zeros(10)
    for i in range(5):
        v_result = np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_validation").astype(float)
        v_rank = np.argsort(-v_result)
        v_found = 0
        count = 0
        result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # print v_rank
        for j in v_rank:
            if j <= size:
                v_found += 1
            count += 1
            ratio = v_found / float(size)
            if 1 <= int(ratio/0.05) <= 10:
                if result[int(ratio/0.05)-1] == 0:
                    result[int(ratio/0.05)-1] = v_found / float(count) * 100
        result = np.array(result)
        # print result
        auc += result
    return np.true_divide(auc, 5)


def cal_validation_result_by_combine(method, size):
    auc = np.zeros(10)
    v_result_1 = np.array([])
    v_result_2 = np.array([])
    for i in range(5):
        tmp_v_result = np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_validation").astype(float)
        tmp_v_result_1 = tmp_v_result[:size]
        tmp_v_result_2 = tmp_v_result[size:]

        v_result_1 = np.concatenate((v_result_1, tmp_v_result_1))
        v_result_2 = np.concatenate((v_result_2, tmp_v_result_2))

    v_result = np.concatenate((v_result_1, v_result_2))
    print v_result.shape
    v_rank = np.argsort(-v_result)
    v_found = 0
    count = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print v_rank
    for j in v_rank:
        if j <= size*5:
            v_found += 1
        count += 1
        ratio = v_found / float(size*5)
        if 1 <= int(ratio / 0.05) <= 10:
            if result[int(ratio / 0.05) - 1] == 0:
                result[int(ratio / 0.05) - 1] = v_found / float(count) * 100
    result = np.array(result)
    return result


def cal_test_result(method, size):
    auc = np.zeros(10)
    v_result = np.zeros(size*201)
    for i in range(5):
        v_result += np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_test").astype(float)
    v_rank = np.argsort(-v_result)
    v_found = 0
    count = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print v_rank
    for j in v_rank:
        if j <= size:
            v_found += 1
        count += 1
        ratio = v_found / float(size)
        if 1 <= int(ratio/0.05) <= 10:
            if result[int(ratio/0.05)-1] == 0:
                result[int(ratio/0.05)-1] = v_found / float(count) * 100
    result = np.array(result)
    return result


# print "logistic regression result over validation set with method 1"
# print cal_validation_result_by_mean("logistic_regression", 197)
# print " "
#
# print "logistic regression result over validation set with method 2"
# print cal_validation_result_by_combine("logistic_regression", 197)
# print " "
#
# print "logistic regression result over test set"
# print cal_test_result("logistic_regression", 204)
# print " "
#
# print "random forest result over validation set with method 1"
# print cal_validation_result_by_mean("random_forest", 197)
# print " "
#
# print "random forest result over validation set with method 2"
# print cal_validation_result_by_combine("random_forest", 197)
# print " "
#
# print "random forest result over test set"
# print cal_test_result("random_forest", 204)

print cal_auc("logistic_regression")
