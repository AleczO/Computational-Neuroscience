import numpy as np
import matplotlib.pyplot as plt


def FitzHugh_Nagumo(dt: float, T: float):
    t_vec = np.arange(0, T, dt)
    N = int(T / dt)

    v_vec = np.array([])
    w_vec = np.array([])
    I_vec = 0.65 * np.ones(N)

    v = 0
    w = 0

    for i in range(N):
        v = (v - (np.pow(v, 3) / 3) - w + I_vec[i]) * dt + v
        w = (0.08 * (0.8 * v + 0.7 - w)) * dt + w

        v_vec = np.append(v_vec, v)
        w_vec = np.append(w_vec, w)

    return t_vec, v_vec

T, V = FitzHugh_Nagumo(0.01, 20)

plt.plot(T, V)
plt.show()
