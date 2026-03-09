import matplotlib.pyplot as plt
import numpy as np

def LI(dt: float, T: float):
    N = int(T / dt)

    E_L = -72
    gL = 4
    C_m = 10

    v = -70

    I = 10.0

    t_rec = np.arange(0, T, dt)
    v_rec = np.zeros(N)

    for t in range(N):
        if t > 200 * (1 / dt):
            I = 0

        v = (-gL * (v - E_L) + I) * (dt / C_m) + v
        v_rec[t] = v
        

    return t_rec, v_rec


T, V = LI(0.01, 300)

plt.plot(T, V)
plt.show()