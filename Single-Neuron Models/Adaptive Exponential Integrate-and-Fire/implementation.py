import matplotlib.pyplot as plt
import numpy as np

def AdEx(dt: float, T: float, ):
    u_vec = np.array([])
    t_vec = np.array([])

    u_rest = -70

    v_rh = -50
    theta_reset = -55
    u_r = -75

    R = 500
    Delta_t = 2

    u = u_rest
    w = 0

    I = 1

    tau_m = 5.0
    
    
    tau_w = 10.0

    a = -0.5
    b = 7
    
    for i in range(int(T / dt)):
        u = (-(u - u_rest) + Delta_t * np.exp((u - v_rh) / Delta_t) - w  +  R * I) * (dt / tau_m) + u
        w = (a * (u - u_rest) - w) * (dt / tau_w) + w

        if u >= theta_reset:
            u = u_r
            w = w + b 
        
        u_vec = np.append(u_vec, u)
        t_vec = np.append(t_vec, i)

    return t_vec, u_vec

T, V = AdEx(0.1, 100)

plt.plot(T, V)
plt.show()


# Todo