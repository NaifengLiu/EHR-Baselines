with open("./data/training/1.csv") as f:
    line = f.readline().rstrip()
    split = line.split(",")
    for i in range(len(split)):
        if split[i] in ['Patient_id',
                        'pat_age_nbr',
                        'chnl_cd',
                        'pay_typ_cd',
                        'mkted_prod_nm',
                        'days_supply_cnt',
                        'pat_pay_amt',
                        'sob_lookback_product_grp',
                        'sob_lookfwd_product_grp',
                        'sob_mono_compliant',
                        'npa_grp_cd', 'diag_grp_nm']:
            print i


