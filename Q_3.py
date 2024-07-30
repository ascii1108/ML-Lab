import numpy as np
def matrix_power(A, m):
    if m < 1:
        return "Exponent must be a positive integer"
    result = A**m
    return result

A = np.array([[2, 1], [1, 2]])
m = 3
print(matrix_power(A, m))