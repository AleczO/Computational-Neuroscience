import numpy as np
import matplotlib.pyplot as plt

dt = 0.01

class V_pre_CLASS:
    def __init__(self, n, m, h, v0):
        self.n = n
        self.m = m
        self.h = h
        self.v = v0

    def U(self, i):
        g = [36.0, 120.0, 0.3]
        E = [-12.0, 115.0, 10.4]

        a = np.array([0.01 * (10 - self.v) / (np.exp((10 - self.v) / 10) - 1), 
                    0.1 * (25 - self.v) / (np.exp((25 - self.v) / 10) - 1), 
                    0.07 * np.exp(-self.v / 20)])
            
        b = np.array([0.125 * np.exp(-self.v / 80), 
                    4.0 * np.exp(-self.v / 18), 
                    1 / (np.exp((30 - self.v) / 10) + 1)])

        self.n = self.n + (a[0] * (1 - self.n) - b[0] * self.n) * dt 
        self.m = self.m + (a[1] * (1 - self.m) - b[1] * self.m) * dt 
        self.h = self.h + (a[2] * (1 - self.h) - b[2] * self.h) * dt 

        self.v = (- g[0] * self.n**4 * (self.v - E[0]) 
                  - g[1] * self.m**3 * self.h * (self.v - E[1]) 
                  - g[2] * (self.v - E[2]) + i) * dt + self.v
    

class C_i_CLASS:
    def __init__(self, c0_i):
        self.c_i = c0_i
        self.c_fast = 0
        self.c_slow = 0
        self.m_Ca = 0.6

    def c_fast_U(self, v):
        A_btn = 1.24
        z_Ca = 2.0
        F = 96487.0
        V_btn = 0.13

        self.c_fast = (- (self.I_Ca(v) * A_btn) / (z_Ca * F * V_btn) + self.J_PMleak() - (self.I_PMCa() * A_btn) / (z_Ca * F * V_btn)) * dt + self.c_fast

        self.m_Ca_U()

    def J_PMleak(self):
        v_leak = 2.66e-6
        c_ext = 2

        return v_leak * (c_ext - self.c_i)

    def I_Ca(self, v):
        rho_Ca = 3.2
        g_Ca = 2.3
        V_Ca = 125.0
        
        return rho_Ca * self.m_Ca**2 * g_Ca * (v - V_Ca)

    def I_PMCa(self):
        v_PMCa = 0.4
        K_PMCa = 0.1

        return v_PMCa * self.c_i**2 / (self.c_i**2 + K_PMCa**2)
    
    def m_Ca_U(self):
        V_mCa = -17.0
        k_mCa = 8.4
        V_m = -70.0
        m_Ca_inf = 1 / (1 + np.exp((V_mCa - V_m) / k_mCa))
        tau_mCa = 10

        self.m_Ca = ((m_Ca_inf - self.m_Ca) / tau_mCa) * dt + self.m_Ca




V_pre = V_pre_CLASS(0, 0, 1, 0)
c_fast= C_i_CLASS(0)
N = int(10 / dt)




V = []
T = []
C_fast = []

I = 6.2

for t in range(N):
    V.append(V_pre.v)
    T.append(t)
    C_fast.append(c_fast.c_fast)

    c_fast.c_fast_U(V_pre.v)
    V_pre.U(I)
    

#plt.plot(T, V)
plt.plot(T, C_fast)
plt.show()
