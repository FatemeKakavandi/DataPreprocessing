import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from load_source import find_data_row, read_csv_from_index

# Example usage
csv_file_path = './Data/FD_derisk_2023-01-23/FD-DIAL_catchai_export_2023-01-23T16-21-16Z_pen020_id30000020_20230721_133839.csv'
data_row_index = find_data_row(csv_file_path)
clm_name = ['dis', 'force', 'time']
if data_row_index != -1:
    print(f'The first row containing [DATA] is at index {data_row_index}.')

    # Read CSV from the identified index and store as a DataFrame
    df = read_csv_from_index(csv_file_path, data_row_index+1,clm_name)
    print('Data as DataFrame:')
    print(df.head())
else:
    print('[DATA] not found in any row.')

df.plot(x=df.columns[0],y=df.columns[1])
plt.show()