# with open("./data/training/1.csv") as f:
#     line = f.readline().rstrip()
#     split = line.split(",")
#     for i in range(len(split)):
#         if split[i] in ['Patient_id',
#                         'pat_age_nbr',
#                         'chnl_cd',
#                         'pay_typ_cd',
#                         'mkted_prod_nm',
#                         'days_supply_cnt',
#                         'pat_pay_amt',
#                         'sob_lookback_product_grp',
#                         'sob_lookfwd_product_grp',
#                         'sob_mono_compliant',
#                         'npa_grp_cd', 'diag_grp_nm']:
#             print i

import csv

q = 0

with open("./data/training/training.csv", "w+") as w:
    for i in range(1, 8):
        with open("./data/training/"+str(i)+".csv", "rb") as f:
            f.readline()
            reader = csv.reader(f)
            for line in reader:
                split = line
                w.write(split[5])
                w.write(',')
                w.write(split[2])
                w.write(',')
                w.write(split[7])
                w.write(',')
                w.write(split[16])
                w.write(',')
                w.write(split[19])
                w.write(',')
                w.write(split[36])
                w.write(',')
                w.write(split[40])
                w.write(',')
                w.write(split[69])
                w.write(',')
                w.write(split[72])
                w.write(',')
                w.write(split[73])
                w.write(',')
                w.write(split[77])
                w.write('\n')





            # for line in f.readlines():
            #     split = line.strip().split(",")
            #     if len(split) != q:
            #         print len(split)
            #         q = len(split)
            #         print line
                # w.write(split[5])
                # w.write(',')
                # w.write(split[2])
                # w.write(',')
                # w.write(split[7])
                # w.write(',')
                # w.write(split[16])
                # w.write(',')
                # w.write(split[19])
                # w.write(',')
                # w.write(split[36])
                # w.write(',')
                # w.write(split[40])
                # w.write(',')
                # w.write(split[69])
                # w.write(',')
                # w.write(split[72])
                # w.write(',')
                # w.write(split[73])
                # w.write(',')
                # w.write(split[77])
                # w.write('\n')

