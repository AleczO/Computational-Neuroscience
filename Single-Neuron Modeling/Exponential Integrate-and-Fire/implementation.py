import matplotlib.pyplot as plt
import numpy as np

def EIF(dt):
    T = np.arange(0, 100 / dt, dt)
    N = T.size

    V_T = -55
    V_Thr = -55
    V_re = -75
    E = -72

    D = 5
    C = 15
    gL = 4

    V = np.zeros(N)
    V[0] = -70

    I = 50.0 * np.ones(N)

    for t in range(N - 1):

        V[t + 1] = (dt / C) * (-(V[t] - E) + D * np.exp((V[t] - V_T) / D) + I[t] / gL) + V[t]
        if V[t] > V_Thr:
            V[t + 1] = V_re
            V[t] = V_Thr

    plt.plot(T, V)
    plt.show()

EIF(0.1)