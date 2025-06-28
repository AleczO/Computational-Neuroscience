import numpy as np
import matplotlib.pyplot as plt

dt = 0.01

class V_pre_CLASS: # Działa
    def __init__(self, n, m, h, v0): 
        self.n = 0
        self.m = m
        self.h = h
        self.v = v0

    def U(self, i):
        g = [36.0, 120.0, 0.3]
        E = [-82.0, 45.0, -59.4]

        a = np.array([0.01 * (-60 - self.v) / (np.exp((-60 - self.v) / 10) - 1), 
                    0.1 * (-45 - self.v) / (np.exp((-45 - self.v) / 10) - 1), 
                    0.07 * np.exp((-self.v - 70) / 20)])
            
        b = np.array([0.125 * np.exp((-self.v - 70) / 80), 
                    4.0 * np.exp((-self.v - 70) / 18), 
                    1 / (np.exp((-40 - self.v) / 10) + 1)])

        self.v = (- g[0] * self.n**4 * (self.v - E[0]) 
                  - g[1] * self.m**3 * self.h * (self.v - E[1]) 
                  - g[2] * (self.v - E[2]) + i) * dt + self.v


        self.n = self.n + (a[0] * (1 - self.n) - b[0] * self.n) * dt 
        self.m = self.m + (a[1] * (1 - self.m) - b[1] * self.m) * dt 
        self.h = self.h + (a[2] * (1 - self.h) - b[2] * self.h) * dt 

class C_i_CLASS: 
    def __init__(self, c0_i):
        self.c_i = c0_i

        # Ca Fast dynamics variables

        self.c_fast = 0.0
        self.m_Ca = 0.8
        
        # Ca Slow dynamics variables
                
        self.c_slow = 0

        self.c_ER = 2

        self.p = 0
        self.q = 30

    # -------------------------------------------- Ca Intracellular update function --------------------------------------------

    def U(self, v):

        self.c_fast_U(v)
        self.c_slow_U()

        self.m_Ca_U(v)
        self.c_ER_U()
        self.c_slow_params_U()

        self.c_i = self.c_fast + self.c_slow 
    # -------------------------------------------- Ca fast update functions --------------------------------------------

 
    def c_fast_U(self, v):
        A_btn = 1.24
        z_Ca = 2.0
        F = 96487.0
        V_btn = 0.13

        self.c_fast = (- (self.I_Ca(v) * A_btn) / (z_Ca * F * V_btn) + self.J_PMleak() - (self.I_PMCa() * A_btn) / (z_Ca * F * V_btn)) * dt + self.c_fast

    def J_PMleak(self):
        v_leak = 2.66e-6
        c_ext = 2.0

        return v_leak * (c_ext - self.c_i)

    def I_Ca(self, v):
        rho_Ca = 3.2
        g_Ca = 2.3
        V_Ca = 125.0    
        
        return rho_Ca * (self.m_Ca**2) * g_Ca * (v - V_Ca)

    def I_PMCa(self):
        v_PMCa = 0.4
        K_PMCa = 0.1

        return v_PMCa * self.c_i**2 / (self.c_i**2 + K_PMCa**2)
    
    def m_Ca_U(self, v):
        V_mCa = -17.0
        k_mCa = 8.4
        m_Ca_inf = 1.0 / (1.0 + np.exp((V_mCa - v) / k_mCa))
        tau_mCa = 0.01

        self.m_Ca = ((m_Ca_inf - self.m_Ca) / tau_mCa) * dt + self.m_Ca

    
    # -------------------------------------------- Ca slow update functions --------------------------------------------


    def c_slow_U(self):
        self.c_slow = (-self.J_chan() - self.J_ERpump() - self.J_ERleak()) * dt + self.c_slow

    def J_chan(self):
        def m_inf():
            d_1 = 0.13
            m_inf = self.p / (self.p + d_1)
            
            return m_inf

        def n_inf():
            d_5 = 82.34
            n_inf = self.c_i / (self.c_i + d_5)

            return n_inf
        
        c_1 = 0.185
        v_1 = 30

        return c_1 * v_1 * m_inf()**3 * n_inf()**3 * self.q**3 * (self.c_i - self.c_ER) 

    def J_ERpump(self):
        v_3 = 90
        k_3 = 0.1

        return  v_3 * (self.c_i**2) / (k_3**2 + self.c_i**2)

    def J_ERleak(self):
        c_1 = 0.185
        v_2 = 0.055

        return c_1 * v_2 * (self.c_i - self.c_ER)


    def c_slow_params_U(self):
        self.p_U()
        self.q_U()


    def c_ER_U(self):
        c_1 = 0.185

        self.c_ER = ( (-1 / c_1) * (- self.J_chan() - self.J_ERpump() - self.J_ERleak()) ) + self.c_ER

    def p_U(self):  
        v_g = 0.062
        g_a = 0.1 # <---- Tu są problemy -  Nie uwzględniono Zachowania Glutaminy - To nie jest stały parametr
        k_g = 0.78
        tau_p = 0.14
        p_0 = 160

        self.p = (v_g * g_a**(0.3) / (k_g**0.3 + g_a**0.3) - tau_p * (self.p - p_0)) * dt + self.p
    
    def q_U(self):
        # Works
        def alpha_q():
            a_2 = 0.2
            d_2 = 1.049
            d_1 = 0.13
            d_3 = 943.4

            return a_2 * d_2 * (self.p + d_1) / (self.p + d_3)

        # Works
        def beta_q():
            a_2 = 0.2
            return a_2 * self.c_i

        self.q = (alpha_q() * (1 - self.q) - beta_q() * self.q) * dt + self.q



class G_CLASS:
    def __init__(self):
        self.R = 0.0
        self.E = 0.0
        self.I = 0.0
        self.g = 0.0

    def R_U(self):
        tau_rec = 800.0
        f_r = 0.5

        self.R = (self.I / tau_rec - f_r * self.R) * dt + self.R

    def E_U(self):
        tau_inact = 3.0
        f_r = 0.5

        self.E = (-self.E / tau_inact + f_r * self.R) * dt + self.E

    def I_U(self):
        self.I = 1.0 - self.R - self.E

    def g_U(self):
        n_v = 2.0
        g_v = 60.0
        g_c = 10.0
        
        self.g = (n_v * g_v * self.E - g_c * self.g) * dt + self.g

V_pre = V_pre_CLASS(0, 0, 1, -70)
c_i = C_i_CLASS(0.1)
N = int(100 / dt)




V = []
T = []
C_fast = []
C_slow = []
C_i = []
MCa = []



I = 8.2

for t in range(N):
    if t > N / 10:
        break

    V.append(V_pre.v)
    T.append(t)
    C_slow.append(c_i.c_slow)
    C_fast.append(c_i.c_fast)
    C_i.append(c_i.c_i)
    MCa.append(c_i.m_Ca)

    V_pre.U(I)
    c_i.U(V_pre.v)




#plt.plot(T, V)
#plt.plot(T, C_fast)
plt.plot(T, C_i)
#plt.plot(T, C_slow)

plt.show()
