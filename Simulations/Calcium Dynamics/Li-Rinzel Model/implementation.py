import numpy as np
import matplotlib.pyplot as plt


dt = 0.01




def DCa(Ca, IP_3, h):
    
    # Ca_ER

    c_0 = 2.0
    c_1 = 0.185

    Ca_ER = (c_0 - Ca) / c_1

    # J_Channel 

    d_1 = 0.13
    m_inf = IP_3 / (IP_3 + d_1)
    
    d_5 = 0.08234
    n_inf = Ca / (Ca + d_5)
        
    c_1 = 0.185
    v_1 = 6.0
    
    J_Channel = (c_1 * v_1 * (m_inf**3) * (n_inf**3) * (h**3) * (Ca - Ca_ER))

    # J_Pump

    v_3 = 0.9
    k_3 = 0.1

    J_Pump = (v_3 *(Ca**2) )/ ((k_3**2) + (Ca**2))


    # J_Leak

    c_1 = 0.185
    v_2 = 0.11

    J_Leak = c_1 * v_2 * (Ca - Ca_ER)
    
    # ----------------

    return (-J_Channel - J_Pump - J_Leak) * dt 




def Dh(Ca, IP_3, h):
    a_2 = 0.2
    d_2 = 1.049
    d_1 = 0.13
    d_3 = 0.9434

    alpha_h = a_2 * d_2 * ((IP_3 + d_1) / (IP_3 + d_3))

    beta_h = a_2 * Ca
    
    dh = (alpha_h * (1 - h) - beta_h * h) * dt
    
    return dh


    
    
N = int(200 / dt)



Ca = np.zeros(N, float)
H = np.zeros(N, float)
T = np.zeros(N, float)

Ca[0] = 0.18
H[0] = 0.6

def IP3(t):
    if 20 < t  < 100:
        return 0.5
    else:
        return 0.0


for t in range(1, N):
    
    Ca[t] = Ca[t - 1] + DCa(Ca[t - 1], IP3(t * dt), H[t - 1])
    H[t] = H[t - 1] + Dh(Ca[t - 1], IP3(t * dt), H[t - 1])
    T[t] = T[t - 1] + dt


plt.plot(T, Ca, label="Calcium in Cytosol")
plt.plot(T, H, label="H gate")
plt.legend()
plt.show()