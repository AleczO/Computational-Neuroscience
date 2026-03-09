import numpy as np
import matplotlib.pyplot as plt


def FitzHugh_Nagumo(dt: float, T: float):
    N = int(T / dt)

    v = 0
    w = 0

    I = 0.65 * np.ones(N)
    
    v_rec = np.array([])
    t_rec = np.arange(0, T, dt)


    for i in range(N):
        v = (v - (np.pow(v, 3) / 3) - w + I[i]) * dt + v
        w = (0.08 * (0.8 * v + 0.7 - w)) * dt + w

        v_rec = np.append(v_rec, v)

    return t_rec, v_rec

T, V = FitzHugh_Nagumo(0.01, 200)

plt.plot(T, V)
plt.show()
