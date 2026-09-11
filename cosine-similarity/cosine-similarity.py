import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    vec_a = np.array(a, dtype=np.float64)
    vec_b = np.array(b, dtype=np.float64)

    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    if norm_a == 0.0 and norm_b == 0.0:
        return 0.0

    dot_product = np.dot(vec_a, vec_b)
    denom = norm_a * norm_b

    if denom == 0.0:
        return 0.0

    similarity = dot_product / denom

    if np.isnan(similarity):
        return 0.0

    return float(similarity)