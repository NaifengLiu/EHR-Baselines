import numpy as np

size = 197


auc = np.zeros(20)
for i in range(5):
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    v_result = np.loadtxt("result/bagging_random_forest/fold_" + str(i + 1) + "_validation_predict").astype(float)
    for j in range(len(v_result)):
        if v_result[j] / float(200) >= 0.5 and j <= size:
            tp += 1
        elif v_result[j] / float(200) >= 0.5 and j > size:
            fp += 1
        elif v_result[j] / float(200) < 0.5 and j <= size:
            fn += 1
        elif v_result[j] / float(200) < 0.5 and j > size:
            tn += 1
    print tp, tn, fp, fn
    print float(tp)/float(tp+fp)
    print float(tp)/float(tp+fn)
