import numpy as np
import matplotlib.pyplot as plt

def Izhikevich(dt: float, T: float, a, b, c, d):
    N = int(T / dt)

    t_vec = np.arange(0, T, dt)
    u_vec = np.zeros(N)
    v_vec = np.zeros(N)

    v_vec[0] = c
    u_vec[0] = c * b

    I = 5.0 * np.ones(N)

    for t in range(N - 1):
        if v_vec[t] >= 30:
            v_vec[t] = c
            u_vec[t] = u_vec[t] + d

        v_vec[t + 1] = (0.04 * pow(v_vec[t], 2) + 5.0 * v_vec[t] + 140.0 - u_vec[t] + I[t]) * dt + v_vec[t]
        u_vec[t + 1] = (a * (b * v_vec[t] - u_vec[t])) * dt + u_vec[t]

    return v_vec, t_vec

V, T = Izhikevich(0.01, 200, 0.02, 0.2, -65.0, 2.0)

plt.plot(T, V)
plt.show()
