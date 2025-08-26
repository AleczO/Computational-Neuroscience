import matplotlib.pyplot as plt
import numpy as np

def EIF(dt: float, T: float):
    N = int(T / dt)

    t_vals = np.arange(0, T, dt)
    u_vals = np.zeros(N)

    
    v_rh = -50
    u_rest = -72
    u_r = -75

    Delta_t = 5
    tau = 15

    theta_reset = -55 

    u = u_rest

    RI = 20.0

    for i in range(N):
        u = ( -(u - u_rest) + Delta_t * np.exp((u - v_rh) / Delta_t) + RI ) * (dt / tau) + u
        if u > theta_reset:
            u = u_r
            
        u_vals[i] = u

    return t_vals, u_vals


T, V = EIF(0.1, 300)

plt.plot(T, V)
plt.show()