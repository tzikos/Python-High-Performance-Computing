import numpy as np

def matmul(A, B):
    C = np.zeros((A.shape[0],B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                C[i,j] += A[i,k] * B[k,j]
    return C

if __name__=='__main__':
    
    A = np.random.rand(100, 100)
    B = np.random.rand(100, 100)

    result = matmul(A, B)

    

