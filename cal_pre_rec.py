import numpy as np
from sklearn import metrics

y = np.array([1, 1, 2, 2])
pred = np.array([0.1, 0.4, 0.35, 0.8])
fpr, tpr, thresholds = metrics.roc_curve(y, pred, pos_label=2)
metrics.auc(fpr, tpr)


def cal_validation_result_by_mean(method):
    auc = np.zeros(10)
    for i in range(5):
        v_result = np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_validation").astype(float)
        v_rank = np.argsort(-v_result)
        v_found = 0
        count = 0
        result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # print v_rank
        for j in v_rank:
            if j <= 197:
                v_found += 1
            count += 1
            ratio = v_found / float(197)
            if 1 <= int(ratio/0.05) <= 10:
                if result[int(ratio/0.05)-1] == 0:
                    result[int(ratio/0.05)-1] = v_found / float(count) * 100
        result = np.array(result)
        # print result
        auc += result
    return np.true_divide(auc, 5)


def cal_validation_result_by_combine(method):
    auc = np.zeros(10)
    v_result_1 = np.array([])
    v_result_2 = np.array([])
    for i in range(5):
        tmp_v_result = np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_validation").astype(float)
        tmp_v_result_1 = tmp_v_result[:197]
        tmp_v_result_2 = tmp_v_result[197:]

        v_result_1 = np.concatenate((v_result_1, tmp_v_result_1))
        v_result_2 = np.concatenate((v_result_2, tmp_v_result_2))

    v_result = np.concatenate((v_result_1, v_result_2))
    v_rank = np.argsort(-v_result)
    v_found = 0
    count = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print v_rank
    for j in v_rank:
        if j <= 985:
            v_found += 1
        count += 1
        ratio = v_found / float(985)
        if 1 <= int(ratio / 0.05) <= 10:
            if result[int(ratio / 0.05) - 1] == 0:
                result[int(ratio / 0.05) - 1] = v_found / float(count) * 100
    result = np.array(result)
    return result


def cal_test_result(method):
    auc = np.zeros(10)
    v_result = np.zeros(41004)
    for i in range(5):
        v_result += np.loadtxt("result/bagging_"+method+"/fold_"+str(i+1)+"_test").astype(float)
    v_rank = np.argsort(-v_result)
    v_found = 0
    count = 0
    result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # print v_rank
    for j in v_rank:
        if j <= 204:
            v_found += 1
        count += 1
        ratio = v_found / float(204)
        if 1 <= int(ratio/0.05) <= 10:
            if result[int(ratio/0.05)-1] == 0:
                result[int(ratio/0.05)-1] = v_found / float(count) * 100
    result = np.array(result)
    return result


# print "logistic regression result over validation set with method 1"
# print cal_validation_result_by_mean("logistic_regression")
# print " "
#
# print "logistic regression result over validation set with method 2"
# print cal_validation_result_by_combine("logistic_regression")
# print " "
#
# print "logistic regression result over test set"
# print cal_test_result("logistic_regression")
# print " "
#
# print "random forest result over validation set with method 1"
# print cal_validation_result_by_mean("random_forest")
# print " "
#
# print "random forest result over validation set with method 2"
# print cal_validation_result_by_combine("random_forest")
# print " "
#
# print "random forest result over test set"
# print cal_test_result("random_forest")
