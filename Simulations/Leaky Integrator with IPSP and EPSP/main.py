import matplotlib.pyplot as plt
import numpy as np
import math

V0 = -72
E = -72

g_L = 4
tau_m = 15

tau_e = 5
tau_i = 3

dt = 0.1
T = np.arange(0, 400, dt)
N = T.size

V = np.zeros(N)
V[0] = V0

I_e = np.zeros(N)
Je = 1000

S_e = np.zeros(N)
S_e[200] = 1
S_e[350] = 1


I_i = np.zeros(N)
Ji = -500

S_i = np.zeros(N)
S_i[600] = 1


for t in range(N - 1):
    V[t + 1] = (dt / tau_m) * (-(V[t] - E) + I_e[t] / g_L + I_i[t] / g_L) + V[t] 
    I_e[t + 1] = (-I_e[t] + Je * S_e[t]) * (dt / tau_e) + I_e[t]
    I_i[t + 1] = (-I_i[t] + Ji * S_i[t]) * (dt / tau_i) + I_i[t]

    
plt.plot(T, V)
plt.show()
