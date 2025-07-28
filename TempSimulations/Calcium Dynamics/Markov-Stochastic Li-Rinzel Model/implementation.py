import numpy as np
import matplotlib.pyplot as plt
import random


dt = 0.01

class Ca_Dynamics:
    
    def __init__(self, Ca_0):
        self.Ca = Ca_0
        self.IP_3 = 0
        self.Ca_ER = 0
        
        self.Nh = np.zeros(30)
    

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
        
        return (c_1 * v_1 * (m_inf**3) * (n_inf**3) * (self.Open_Channels() / self.Nh.size) * (self.Ca - self.Ca_ER))
    
    def Open_Channels(self):
        cnt = 0
        for h in self.Nh:
            if h == 3:
                cnt += 1
                
        return cnt
        
    
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

        Ah = a_2 * d_2 * ((self.IP_3 + d_1) / (self.IP_3 + d_3))

        Bh = a_2 * self.Ca
        
        
        P = np.array([[1 - 3 * Ah * dt ,            3 * Bh * dt ,                       0 ,                    0],
                      [       Bh *  dt , 1 - (Bh + 2 * Ah) * dt ,             2 * Ah * dt ,                    0],
                      [              0 ,            2 * Bh * dt ,  1 - (Ah + 2 * Bh) * dt ,              Ah * dt],
                      [              0 ,                      0 ,             3 * Bh * dt ,      1 - 3 * Bh * dt]])
        
        
        for h in range(self.Nh.size):
            self.Nh[h] = random.choices([0,1,2,3], P[int(self.Nh[h])], k=1)[0]
        

# random.seed(1e9 + 7)

Ca = Ca_Dynamics(0.18)

N = int(200 / dt)

T = []
CaT = []
NOpenT = []

Ca.IP_3 = 0.3

for t in range(N):
    
    Ca.Ca_U()
    Ca.Ca_ER_U()
    Ca.h_U()
    
    T.append(t)
    CaT.append(Ca.Ca)
    

    
plt.plot(T, CaT)
plt.grid()
plt.show()
