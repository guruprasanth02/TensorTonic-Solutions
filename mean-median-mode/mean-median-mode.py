from collections import Counter
import numpy as np
from scipy import stats

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mean_val = float(np.mean(x))
    median_val = float(np.median(x))
    mode_result = stats.mode(x, keepdims=True)
    mode_val = float(mode_result.mode[0])
    return {
        "mean": mean_val,
        "median": median_val,
        "mode": mode_val
    }