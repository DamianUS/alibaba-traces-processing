import pandas as pd
import os

days = range(1, 9)
strides = [1, 3, 30]
strided_seconds = [stride*10 for stride in strides]

for strided_second in strided_seconds:
    dfs = [pd.read_csv(f'data/grouped_by_timestamp/day_{day}/machine_usage_day_{day}_grouped_{strided_second}_seconds.csv') for day in days]
    concated_df = pd.concat(dfs)
    concated_df.to_csv(f'data/grouped_by_timestamp/machine_usage_days_{min(days)}_to_{max(days)}_grouped_{strided_second}_seconds.csv', index=False)

