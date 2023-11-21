import numpy as np

def interpolate_and_extrapolate(displacement, force, min_range, max_range):
    # Ensure that the displacement array is sorted
    sorted_indices = np.argsort(displacement)
    displacement = displacement[sorted_indices]
    force = force[sorted_indices]

    # Find the indices within the specified range
    within_range_indices = np.where((displacement >= min_range) & (displacement <= max_range))[0]

    # Interpolate within the specified range
    interpolated_force_within_range = np.interp(displacement[within_range_indices],
                                                displacement[within_range_indices],
                                                force[within_range_indices])

    # Extrapolate outside the specified range
    extrapolated_force_below_range = np.interp(min_range, displacement[within_range_indices],
                                               interpolated_force_within_range, left=np.nan)
    extrapolated_force_above_range = np.interp(max_range, displacement[within_range_indices],
                                               interpolated_force_within_range, right=np.nan)

    # Combine the results
    interpolated_and_extrapolated_force = np.concatenate([
        np.array([extrapolated_force_below_range]),
        interpolated_force_within_range,
        np.array([extrapolated_force_above_range])
    ])

    return displacement, interpolated_and_extrapolated_force

# Example usage:
# Replace this with your actual displacement and force data
displacement_data = np.array([0, 1, 2, 3, 4, 5])
force_data = np.array([10, 12, 15, 20, 25, 30])

# Define the min and max range for interpolation and extrapolation
min_range = 1
max_range = 4

# Perform interpolation and extrapolation
new_displacement, new_force = interpolate_and_extrapolate(displacement_data, force_data, min_range, max_range)

# Print the results
print("Original Data:")
print("Displacement:", displacement_data)
print("Force:", force_data)

print("\nInterpolated and Extrapolated Data:")
print("Displacement:", new_displacement)
print("Force:", new_force)
