import matplotlib.pyplot as plt
import numpy as np
import math

dt = 0.1
T = np.arange(0, 400, dt)
N = T.size

E = -72
g_L = 4
Cm = 30

V = np.zeros(N)
V[0] = -70

I = 10.0

for t in range(N - 1):
    if t > 200 * (1 / dt):
        I = 0
    
    V[t + 1] = (dt / Cm) * (-g_L*( V[t] - E) + I) + V[t]
    
plt.plot(T, V)
plt.show()
