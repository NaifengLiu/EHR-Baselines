# with open("diag_grp_1M.csv") as f:
#     title = f.readline()
#     with open("output.csv", "w+") as w:
#         w.write(title)
#         for lines in f.readlines():
#             w.write(lines.)
#
#
#
#
#
import numpy as np

a = np.array([1, 2, 3])
b = np.array([3, 4, 5])
c = np.array([5, 6, 7])

print np.stack((a, b, c)).T[1][1]


