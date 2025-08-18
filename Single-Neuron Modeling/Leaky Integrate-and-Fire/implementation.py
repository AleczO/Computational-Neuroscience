import numpy as np
import matplotlib.pyplot as plt

def LIF(dt: float, T: float):
    tau = 10 
    u_rest = -65 
    u_r = -70

    theta_reset = -55 

    u = u_rest
    RI = 30

    u_vec = np.array([])
    t_vec = np.array([])

    for i in range(int(T / dt)):
        u = (-(u - u_rest) + RI) * (dt / tau) + u
        if u >= theta_reset:
            u = u_r

        u_vec = np.append(u_vec, u)
        t_vec = np.append(t_vec, i)


    return u_vec, t_vec


v, t = LIF(0.1, 100)
plt.plot(t, v)
plt.show()