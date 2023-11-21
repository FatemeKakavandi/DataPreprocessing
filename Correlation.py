import numpy as np
from scipy.interpolate import interp1d
from load_source import load_single_file,get_all_files_with_extension
from Low_corr_values import find_indices_below_threshold
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def interpolate_and_downsample(displacement, force, dis_min, dis_max, target_length=1000):
    # Create an interpolation function
    interp_func = interp1d(displacement, force, kind='linear', fill_value='extrapolate')

    # Generate new displacement values
    new_displacement = np.linspace(dis_min, dis_max, target_length)

    # Interpolate force values at the new displacement points
    new_force = interp_func(new_displacement)

    return new_displacement, new_force

# Dataframe labels
dis_label = 'dis'
force_label = 'force'
time_label = 'time'

clm_name = [dis_label,force_label,time_label]


## Loading all the CSV files
directory = './Data/FD_derisk_2023-01-23'
files = get_all_files_with_extension(directory,extension='.csv')


# Data length
smp_length = 1000
Dial_dis_min = -53
Dial_dis_max = -41
th =  0.05
final_dial_df = pd.DataFrame()
for file in files:
    if 'DIAL' in file:
        #print(file)
        data_label = file.split('/')[-1].split('.csv')[0]
        dial_df = load_single_file(file,clm_name)
        dis_min = dial_df[dis_label].min()
        dis_max = dial_df[dis_label].max()

        new_dis, new_force = interpolate_and_downsample(np.array(dial_df[dis_label]), np.array(dial_df[force_label]),
                                                            dis_min, dis_max, smp_length)

        force_df = pd.DataFrame(new_force,columns=[data_label])

        final_dial_df = pd.concat([final_dial_df,force_df],ignore_index=True,axis=1)


corr_matrix = final_dial_df.corr()
corr_matrix = corr_matrix.to_numpy().mean(axis=0)
indx_list = np.where(corr_matrix<0.9)[0]
print(indx_list)
for elm in indx_list:
    plt.plot(final_dial_df[final_dial_df.columns[elm]])

plt.show()
#indx_list = find_indices_below_threshold(corr_matrix,0.5)
#print(indx_list)

#print(final_corr_matrix)
#sns.heatmap(final_corr_matrix, cmap=None, annot=None)