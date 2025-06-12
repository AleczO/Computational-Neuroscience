import matplotlib.pyplot as plt
import numpy as np
import math

V0 = -70
V_T = -55
V_Thr = -10
V_re = -75
E = -72

D = 5
g_L = 4
tau_m = 15

dt = 0.1
T = np.arange(0, 400, dt)
N = T.size

V = np.zeros(N)
V[0] = V0

I = 400.0 * np.ones(N)

for i in range(len(I)):
    I[i] = I[i] / 5


for t in range(N - 1):
    if t > 200 * (1 / dt):
        I[t] = 0
    
    V[t + 1] = (dt / tau_m) * (-( V[t] - E) + D * math.exp((V[t] - V_T) / D) + I[t] / g_L) + V[t] 
    if V[t] > V_Thr:
        V[t + 1] = V_re
        V[t] = V_Thr
        
    
plt.plot(T, V)
plt.show()
