import numpy as np
import matplotlib.pyplot as plt

def LIF(dt: float, T: float):
    N = int(T / dt)

    
    tau = 10 
    u_rest = -65 
    u_r = -70

    theta_reset = -55 

    u = u_rest
    RI = 30

    t_rec = np.arange(0, T, dt)
    u_rec = np.zeros(N)

    for i in range(N):
        u = (-(u - u_rest) + RI) * (dt / tau) + u
        if u >= theta_reset:
            u = u_r

        u_rec[i] = u

    return u_rec, t_rec


v, t = LIF(0.1, 100)
plt.plot(t, v)
plt.show()