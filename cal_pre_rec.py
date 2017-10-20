import numpy as np
from sklearn import metrics
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
# import matplotlib as mpl
# mpl.use('Agg')
# import matplotlib.pyplot as plt


def cal_auc(method):
    v_result = np.zeros(41004)
    for i in range(5):
        v_result += np.loadtxt("result/bagging_" + method + "/fold_" + str(i + 1) + "_test").astype(float)
    pred = np.true_divide(v_result, 200)
    y = np.concatenate((np.zeros(204) + 1, np.zeros(204*200)), axis=0)
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
    print v_result[v_rank[0]]
    print v_result[v_rank[1]]
    print v_result[v_rank[2]]
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


def cal_pr(method):
    v_result_1 = np.array([])
    v_result_2 = np.array([])
    for i in range(5):
        tmp_v_result = np.loadtxt("result/bagging_" + method + "/fold_" + str(i + 1) + "_validation").astype(float)
        tmp_v_result_1 = tmp_v_result[:197]
        tmp_v_result_2 = tmp_v_result[197:]

        v_result_1 = np.concatenate((v_result_1, tmp_v_result_1))
        v_result_2 = np.concatenate((v_result_2, tmp_v_result_2))

    v_score = np.concatenate((v_result_1, v_result_2))
    print v_score.shape
    y_test = np.concatenate((np.zeros(985) + 1, np.zeros(985*200)), axis=0)
    precision, recall, thresholds = precision_recall_curve(y_test, np.true_divide(v_score, 200))
    # plt.step(recall, precision, color='b', alpha=0.2,
    #          where='post')
    # plt.fill_between(recall, precision, step='post', alpha=0.2,
    #                  color='b')
    #
    # plt.xlabel('Recall')
    # plt.ylabel('Precision')
    # plt.ylim([0.0, 1.05])
    # plt.xlim([0.0, 1.0])
    # plt.savefig("tmp")


# cal_pr("logistic_regression_lasso")


# print "logistic regression result over validation set with method 1"
# print cal_validation_result_by_mean("logistic_regression", 197)
# print " "
#
# print "logistic regression result over validation set with method 2"
# print cal_validation_result_by_combine("logistic_regression", 197)
# print " "
#
# print "logistic regression result over test set"
# print cal_test_result("logistic_regression", 248)
# print " "
#
print "logistic regression result over validation set with method"
print cal_validation_result_by_combine("logistic_regression_lasso", 197)
print " "

print "logistic regression result over test set"
print cal_test_result("logistic_regression_lasso", 248)
print " "
#
# print "random forest result over validation set with method 1"
# print cal_validation_result_by_mean("random_forest", 197)
# print " "
# #
# print "random forest result over validation set with method 2"
# print cal_validation_result_by_combine("random_forest", 197)
# print " "
# #
# print "random forest result over test set"
# print cal_test_result("random_forest", 248)
#
# print cal_auc("logistic_regression")
