import numpy as np


dt = 0.1
T = np.arange(0, 100 * (1 / dt), dt)
N = T.size


def c_fast_fun(c_f, c_i):
    A_btn = 1.24
    z_Ca = 2.0
    F = 96487.0
    V_btn = 0.13

    return (- (I_Ca(c_f) * A_btn) / (z_Ca * F * V_btn) + J_PMleak() - (I_PMCa(c_f) * A_btn) / (z_Ca * F * V_btn)) * dt + c_f


def J_PMleak(c_i):
    v_leak = 2.66e-6
    c_ext = 2

    return v_leak * (c_ext - c_i)


def I_PMCa(c_i):
    v_PMCa = 0.4
    K_PMCa = 0.1

    return v_PMCa * c_i**2 / (c_i**2 + K_PMCa**2)


def I_Ca(t):
    rho_Ca = 3.2
    g_Ca = 2.3
    V_Ca = 125.0
    
    return rho_Ca * m_Ca(t)**2 * g_Ca * (V_pre(t) - V_Ca)


def m_Ca():
    V_mCa = -17.0
    k_mCa = 8.4
    V_m = -70.0
    m_Ca_inf = 1 / (1 + np.exp((V_mCa - V_m) / k_mCa))





def V_pre(v, i):
    g = [36.0, 120.0, 0.3]
    E = [-12.0, 115.0, 10.4]

    m, n, h = 0, 0, 1


    a = np.array([0.01 * (10 - v) / (np.exp((10 - v) / 10) - 1), 
                0.1 * (25 - v) / (np.exp((25 - v) / 10) - 1), 
                0.07 * np.exp(-v / 20)])
        
    b = np.array([0.125 * np.exp(-v / 80), 
                4.0 * np.exp(-v / 18), 
                1 / (np.exp((30 - v) / 10) + 1)])

    n =  n + (a[0] * (1 - n) - b[0] * n) * dt 
    m =  m + (a[1] * (1 - m) - b[1] * m) * dt 
    h =  h + (a[2] * (1 - h) - b[2] * h) * dt 

    return (- g[0] * n**4 * (v - E[0]) - g[1] * m**3 * h * (v - E[1]) - g[2] * (v - E[2]) + i) * dt + v 

   





V = np.zeros(N)
I = 6.2 * np.ones(N)

c_i = np.zeros(N)
c_fast = np.zeros(N)
c_slow = np.zeros(N)

for k in range(N - 1):

    

    c_fast[k + 1] = c_fast_fun(c_fast[k], c_i[k]) 
    c_slow[k + 1] = 5 
    c_i[k + 1] = (c_fast[k + 1] - c_fast[k]) + (c_slow[k + 1] - c_slow[k]) + c_i[k]


