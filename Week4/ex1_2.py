import numpy as np

def outer(vec1,vec2):
    result = np.array([[vec1[i] * vec2[j] for j in range(len(vec2))] for i in range(len(vec1))])
    
    return result