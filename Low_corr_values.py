import numpy as np

def find_indices_below_threshold(arr, threshold):
    """
    Find the indices of elements in the array that are below the threshold.

    Parameters:
    - arr: NumPy array
    - threshold: Threshold value

    Returns:
    - List of tuples representing the indices of elements below the threshold
    """
    below_threshold_indices = np.where(arr < threshold)
    indices = list(zip(below_threshold_indices[0], below_threshold_indices[1]))
    return indices

# Example usage:
# Create a sample 2D NumPy array
example_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define a threshold
threshold_value = 5

# Find indices below the threshold
result_indices = find_indices_below_threshold(example_array, threshold_value)

# Print the result
print(f"Indices below threshold {threshold_value}: {result_indices}")
