import numpy as np
import matplotlib.pyplot as plt

def HH(dt: float, T: float):
    N = int(T / dt)
   
    g = [36.0, 120.0, 0.3]
    E = [-12.0, 115.0, 10.4]

    m, n, h = 0, 0, 1

    v = 0


    I = 6.2 * np.ones(N)
    v_rec = np.array([])
    t_rec = np.arange(0, T, dt)


    for t in range(N):
        a = np.array([0.01 * (10 - v) / (np.exp((10 - v) / 10) - 1),
                    0.1 * (25 - v) / (np.exp((25 - v) / 10) - 1),
                    0.07 * np.exp(-v / 20)])

        b = np.array([0.125 * np.exp(-v / 80),
                    4.0 * np.exp(-v / 18),
                    1 / (np.exp((30 - v) / 10) + 1)])

        n = n + (a[0] * (1 - n) - b[0] * n) * dt
        m = m + (a[1] * (1 - m) - b[1] * m) * dt
        h = h + (a[2] * (1 - h) - b[2] * h) * dt

        v = (- g[0] * n ** 4 * (v - E[0])
                    - g[1] * m ** 3 * h * (v - E[1])
                    - g[2] * (v - E[2])
                    + I[t]) * dt + v
        
        v_rec = np.append(v_rec, v)

    return v_rec, t_rec

v, t = HH(0.01, 100)

plt.plot(t, v)
plt.show()
