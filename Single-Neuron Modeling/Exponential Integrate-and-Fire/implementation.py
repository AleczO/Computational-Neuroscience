import matplotlib.pyplot as plt
import numpy as np

def EIF(dt: float, T: float):
    N = int(T / dt)

    t_vec = np.array([])
    u_vec = np.array([])

    
    v_rh = -50
    u_rest = -72
    u_r = -75

    Delta_t = 5
    tau = 15

    theta_reset = -55 

    u = u_rest

    RI = 15.0

    for t in range(N - 1):
        u = ( -(u - u_rest) + Delta_t * np.exp((u - v_rh) / Delta_t) + RI ) * (dt / tau) + u
        if u > theta_reset:
            u = u_r
            
        u_vec = np.append(u_vec, u)
        t_vec = np.append(t_vec, t)

    return t_vec, u_vec


T, V = EIF(0.1, 300)

plt.plot(T, V)
plt.show()