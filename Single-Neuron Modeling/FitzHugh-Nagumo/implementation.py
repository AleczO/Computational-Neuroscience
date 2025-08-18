import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
T = np.arange(0, 10 / dt, dt)
N = T.size

V = np.zeros(N)
W = np.zeros(N)
I = 0.65 * np.ones(N)

for t in range(N - 1):
    V[t + 1] = (V[t] - (V[t]**3 / 3) - W[t] + I[t]) * dt + V[t]
    W[t + 1] = (0.08 * (0.8 * V[t] + 0.7 -  W[t])) * dt + W[t]

plt.plot(T, V)
plt.show()
