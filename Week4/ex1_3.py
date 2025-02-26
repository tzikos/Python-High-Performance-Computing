import numpy as np

def distmat_1d(vec1, vec2):

    vec1 = vec1[:, None]
    vec2 = vec2[None, :]

    result = np.abs(vec2-vec1)

    return result