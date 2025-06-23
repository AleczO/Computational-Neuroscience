import numpy as np
import matplotlib.pyplot as plt

dt = 0.01
T = np.arange(0, 1 / dt, dt)
N = T.size

V = np.zeros(N)
I = 6.2 * np.ones(N)

g = [36.0, 120.0, 0.3]
E = [-12.0, 115.0, 10.4]


m, n, h = 0, 0, 1


for t in range(N - 1):
    a = np.array([0.01 * (10 - V[t]) / (np.exp((10 - V[t]) / 10) - 1), 
                  0.1 * (25 - V[t]) / (np.exp((25 - V[t]) / 10) - 1), 
                  0.07 * np.exp(-V[t] / 20)])
    
    b = np.array([0.125 * np.exp(-V[t] / 80), 
                  4.0 * np.exp(-V[t] / 18), 
                  1 / (np.exp((30 - V[t]) / 10) + 1)])

    n =  n + (a[0] * (1 - n) - b[0] * n) * dt 
    m =  m + (a[1] * (1 - m) - b[1] * m) * dt 
    h =  h + (a[2] * (1 - h) - b[2] * h) * dt 

    V[t + 1] = (- g[0] * n**4 * (V[t] - E[0]) 
                - g[1] * m**3 * h * (V[t] - E[1]) 
                - g[2] * (V[t] - E[2]) 
                + I[t]) * dt + V[t] 
    
plt.plot(T, V)
plt.show()
