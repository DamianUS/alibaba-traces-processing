import pandas as pd
import os

days = range(1, 9)
strides = [3, 30]
strided_seconds = [stride*10 for stride in strides]

for day in days:
    generated_data_directory_name = f'data/grouped_by_timestamp/day_{day}/'
    os.makedirs(generated_data_directory_name, exist_ok=True)
    df = pd.read_csv(f'data/machine_usage_day_{day}.csv', names=["machine_id", "time_stamp", "cpu_util_percent", "mem_util_percent", "mem_gps", "mkpi", "net_in", "net_out", "disk_io_percent"])
    df = df.drop(['machine_id', 'mem_gps', 'mkpi'], axis=1)
    df = df.groupby('time_stamp', axis=0).mean()
    dfs_strided = [df.iloc[range(0,df.shape[0], stride)] for stride in strides]
    df.to_csv(f'{generated_data_directory_name}machine_usage_day_{day}_grouped_10_seconds.csv', index=False)
    for i, df_strided in enumerate(dfs_strided):
        df_strided.to_csv(f'{generated_data_directory_name}machine_usage_day_{day}_grouped_{strided_seconds[i]}_seconds.csv', index=False)
