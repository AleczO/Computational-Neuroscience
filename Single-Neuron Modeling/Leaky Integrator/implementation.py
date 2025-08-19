import matplotlib.pyplot as plt
import numpy as np

def LI(dt: float, T: float):
    t_vec = np.arange(0, T, dt)
    N = int(T / dt)

    E = -72
    gL = 4
    C_m = 10

    v_vec = np.array([])
    v = -70

    I = 10.0

    for t in range(N):
        if t > 200 * (1 / dt):
            I = 0

        
        v = (-gL * (v - E) + I) * (dt / C_m) + v
        v_vec = np.append(v_vec, v)
        

    return t_vec, v_vec


T, V = LI(0.01, 100)

plt.plot(T, V)
plt.show()