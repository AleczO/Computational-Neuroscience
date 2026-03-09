import numpy as np
import matplotlib.pyplot as plt

def Izhikevich(dt: float, T: float, a, b, c, d):
    N = int(T / dt)

    v = c
    u = c * b

    I = 5.0 * np.ones(N)

    v_rec = np.zeros(N)
    t_rec = np.arange(0, T, dt)

    for t in range(N):
        if v >= 30:
            v = c
            u = u + d

        v = (0.04 * np.pow(v, 2) + 5.0 * v + 140.0 - u + I[t]) * dt + v
        u = (a * (b * v - u)) * dt + u
        
        v_rec[t] = v


    return v_rec, t_rec

V, T = Izhikevich(0.01, 200, 0.02, 0.2, -65.0, 2.0)

plt.plot(T, V)
plt.show()
