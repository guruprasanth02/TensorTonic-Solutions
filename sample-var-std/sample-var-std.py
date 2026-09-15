import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    arr = np.array(x, dtype=float)
    varience_val = float(np.var(arr, ddof = 1))
    standard = float(np.std(arr, ddof = 1))

    return {
        "variance": varience_val,
        "standard_deviation": standard
    }