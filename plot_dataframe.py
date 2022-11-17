import matplotlib.pyplot as plt
import pandas as pd
import os

seconds_stride = [10, 30, 300]
days = range(1,9)

for day in days:
    for second_stride in seconds_stride:
        generated_data_directory_name = f'data/grouped_by_timestamp/day_{day}/'
        figures_directory_name = f'data/grouped_by_timestamp/day_{day}/figures/{second_stride}_seconds/'
        concated_figures_directory_name = f'data/grouped_by_timestamp/figures/{second_stride}_seconds/'
        os.makedirs(figures_directory_name, exist_ok=True)
        os.makedirs(concated_figures_directory_name, exist_ok=True)
        df = pd.read_csv(f'{generated_data_directory_name}machine_usage_day_{day}_grouped_{second_stride}_seconds.csv')
        concated_df = pd.read_csv(f'data/grouped_by_timestamp/machine_usage_days_{min(days)}_to_{max(days)}_grouped_{second_stride}_seconds.csv')
        column_names = df.columns
        for column_name in column_names:
            plot_data = df[column_name]
            #axis = [0, plot_data.shape[0], plot_data.min(), plot_data.max()]
            axis = [0, plot_data.shape[0], 0, 100]
            plt.rcParams["figure.figsize"] = (18, 3)
            f, ax = plt.subplots(1)
            plt.plot(plot_data, c="blue", label="Original data", linewidth=1)
            plt.axis(axis)
            plt.title(column_name)
            plt.xlabel('time')
            plt.ylabel(column_name)
            ax.legend()
            plt.savefig(f'{figures_directory_name}{column_name}_usage_day_{day}_grouped_{second_stride}_seconds.pdf')
            plt.close()
            plt.clf()

            plot_data_merged = concated_df[column_name]
            axis = [0, plot_data_merged.shape[0], 0, 100]
            f, ax = plt.subplots(1)
            plt.plot(plot_data_merged, c="blue", label="Original data", linewidth=1)
            plt.axis(axis)
            plt.title(column_name)
            plt.xlabel('time')
            plt.ylabel(column_name)
            ax.legend()
            plt.savefig(f'{concated_figures_directory_name}{column_name}_usage_days_{min(days)}_to_{max(days)}_grouped_{second_stride}_seconds.pdf')
            plt.close()
            plt.clf()

