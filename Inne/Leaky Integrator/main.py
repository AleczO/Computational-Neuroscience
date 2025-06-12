import matplotlib.pyplot as plt
import numpy as np
import math


V0 = -70
V_Thr = 64
E_L = -72
g_L = 4
tau_m = 15

dt = 0.1
T = np.arange(0, 400, dt)
N = T.size


V = np.zeros(N)
V[0] = V0

I = 400.0 * np.ones(N)

for t in range(N - 1):
    if t > 200 * (1 / dt):
        I[t] = 0
    
    dV = (dt / tau_m) * (-( V[t] - E_L) + I[t] / g_L)
    V[t + 1] = V[t] + dV
    

plt.plot(T, V)
plt.show()
