import numpy as np

v_result = np.loadtxt("result/fold_1_validation").astype(int)

v_rank = np.argsort(-v_result)

print v_result[v_rank[0]]
print v_rank[0]

for i in v_result:
    print i

# v_rank_final = v_rank
# v_found = 0
# count = 0
# result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in v_rank_final:
#     if i <= 197:
#         v_found += 1
#     count += 1
#     ratio = v_found / float(197)
#     if 1 <= int(ratio/0.05) <= 10:
#         if result[int(ratio/0.05)-1] == 0:
#             result[int(ratio/0.05)-1] = v_found / float(count) * 100
# print result