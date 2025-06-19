import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T = np.arange(0, 100 * (1 / dt), dt)
N = T.size

U = np.zeros(N)
V = np.zeros(N)

a = 0.02
b = 0.2
c = -65.0
d = 2.0

V[0] = c
U[0] = c * b

I = 5.0 * np.ones(N)


for t in range(N - 1):
    if V[t] >= 30:
        V[t] = c
        U[t] = U[t] + d

    V[t + 1] = (0.04 * pow(V[t], 2) + 5.0 * V[t] + 140.0 - U[t] + I[t]) * dt + V[t]
    U[t + 1] = (a * (b * V[t] - U[t])) * dt + U[t]
    

plt.plot(T, V)
plt.show()
