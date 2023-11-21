import numpy as np
from scipy.interpolate import interp1d
from load_source import load_single_file
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def interpolate_and_downsample(displacement, force, target_length=1000):
    # Create an interpolation function
    interp_func = interp1d(displacement, force, kind='linear', fill_value='extrapolate')

    # Generate new displacement values
    new_displacement = np.linspace(-53, -41, target_length)

    # Interpolate force values at the new displacement points
    new_force = interp_func(new_displacement)

    return new_displacement, new_force

# Dataframe labels
dis_label = 'dis'
force_label = 'force'
time_label = 'time'

clm_name = [dis_label,force_label,time_label]
file_path = 'Data/FD_derisk_2023-01-23/FD-DIAL_catchai_export_2023-01-23T16-21-16Z_pen020_id30000020_20230721_133839.csv'
df = load_single_file(file_path,clm_name)
# Example usage:
# Replace these arrays with your actual force and displacement signals
original_displacement = np.array(df[dis_label])
original_force = np.array(df[force_label])

# Set the target length for downsampling (e.g., 1000)
target_length = 1000

# Interpolate and downsample
new_displacement, new_force = interpolate_and_downsample(original_displacement, original_force, target_length)

# Plot data
plt.plot(original_displacement,original_force,label='original')
plt.plot(new_displacement,new_force,label='new')
plt.legend()
plt.show()
