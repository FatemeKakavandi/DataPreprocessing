import pandas as pd
import numpy as np
from load_source import get_all_files_with_extension, load_single_file

## Loading all the CSV files
directory = './Data/FD_derisk_2023-01-23'
files = get_all_files_with_extension(directory,extension='.csv')

# Dataframe labels
dis_label = 'dis'
force_label = 'force'
time_label = 'time'

clm_name = [dis_label,force_label,time_label]

# Data length
smp_length = 1000

for file in files:
    if 'DIAL' in file:
        dial_df = load_single_file(file,clm_name)
        dial_df[dis_label].min()
        print(dial_df.head())