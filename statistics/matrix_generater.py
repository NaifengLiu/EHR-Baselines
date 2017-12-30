import numpy as np

all_days = np.arange('2010-01-01', '2015-07-31', dtype='datetime64[D]')

day_dict = dict()
for day in all_days:
    day_dict[str(day).replace("-", "")] = 0

