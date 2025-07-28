import numpy as np
import matplotlib.pyplot as plt


dt = 0.01

class Ca_Dynamics:
    
    def __init__(self, Ca_0, h_0):
        self.Ca = Ca_0
        self.IP_3 = 0
        self.Ca_ER = 0
        
        self.h = h_0
    

    def Ca_U(self):
        self.Ca = (-self.J_Channel() - self.J_Pump() - self.J_Leak()) * dt + self.Ca


    def Ca_ER_U(self):
        c_0 = 2.0
        c_1 = 0.185

        self.Ca_ER = (c_0 - self.Ca) / c_1
        

    def J_Channel(self):
        d_1 = 0.13
        m_inf = self.IP_3 / (self.IP_3 + d_1)
        
        d_5 = 0.08234
        n_inf = self.Ca / (self.Ca + d_5)
            
        c_1 = 0.185
        v_1 = 6.0
        
        return (c_1 * v_1 * (m_inf**3) * (n_inf**3) * (self.h**3) * (self.Ca - self.Ca_ER))
        
    
    def J_Pump(self):
        v_3 = 0.9
        k_3 = 0.1

        return (v_3 *(self.Ca**2) )/ ((k_3**2) + (self.Ca**2))
        
        
    def J_Leak(self):
        c_1 = 0.185
        v_2 = 0.11

        return c_1 * v_2 * (self.Ca - self.Ca_ER)
        

    def h_U(self):
        a_2 = 0.2
        d_2 = 1.049
        d_1 = 0.13
        d_3 = 0.9434

        alpha_h = a_2 * d_2 * ((self.IP_3 + d_1) / (self.IP_3 + d_3))

        beta_h = a_2 * self.Ca
        
        self.h = (alpha_h * (1 - self.h) - beta_h * self.h) * dt + self.h


Ca = Ca_Dynamics(0.05, 0.6)

N = int(200 / dt)

T = []
CaT = []
hT = []

for t in range(N):
    
    if 50 < t * dt < 100:
        Ca.IP_3 = 0.45
    else:
        Ca.IP_3 = 0.0 
    
    Ca.Ca_U()
    Ca.Ca_ER_U()
    Ca.h_U()
    
    T.append(t)
    hT.append(Ca.h)
    CaT.append(Ca.Ca)
    

    
plt.plot(T, CaT)
plt.plot(T, hT)
plt.grid()
plt.show()
