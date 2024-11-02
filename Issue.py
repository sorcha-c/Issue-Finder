import numpy as np

def calculate_mean(values):
    """Calculate the mean of a list of values."""
    total = sum(values)
    count = len(values)
    return total / count

def find_max_value(values):
    """Find the maximum value in a list of values."""
    max_value = values[0]
    for value in values:
        if value > max_value:
            max_value = value
    return max_value

def normalize_array(arr):
    """Normalize a numpy array to be between 0 and 1."""
    min_value = np.min(arr)
    max_value = np.max(arr)
    return (arr - min_value) / max_value
