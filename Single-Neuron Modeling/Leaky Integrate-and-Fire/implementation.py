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

    t_vals = np.arange(0, T, dt)
    u_vals = np.zeros(N)

    for i in range(N):
        u = (-(u - u_rest) + RI) * (dt / tau) + u
        if u >= theta_reset:
            u = u_r

        u_vals[i] = u

    return u_vals, t_vals


v, t = LIF(0.1, 100)
plt.plot(t, v)
plt.show()