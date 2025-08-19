import matplotlib.pyplot as plt
import numpy as np

def AdEx(dt: float, T: float):
    
    u_vec = np.array([])
    t_vec = np.array([])

    u_rest = -70

    v_rh = -50
    u_r = -55

    R = 50
    Delta_t = 2

    u = u_rest
    w = 0

    I = 0

    tau_m = 200
    tau_w = 30

    a = 0
    b = 60

    Sigma = 1
    
    for i in range(int(T / dt)):
        u = (-(u - u_rest) + Delta_t * np.exp((u - v_rh) / Delta_t) - R * w  +  R * I) * (dt / tau_m) + u
        w = (a * (u - u_rest) - w + b * tau_w * Sigma) * (dt / tau_m) + w

        if u >= v_rh:
            u = u_r
            Sigma += 1
        
        u_vec = np.append(u_vec, u)
        t_vec = np.append(t_vec, i)

    return t_vec, u_vec

T, V = AdEx(0.01, 10)

plt.plot(T, V)
plt.show()


# Todo