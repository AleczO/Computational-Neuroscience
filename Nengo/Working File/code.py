import numpy as np

n = 10
R = 1

i = np.linspace(-R, R, n)
print(i, '\n')

e = np.tile([[1], [-1]], (n // 2, 1))
print(e)
print(i * e[:, 0])