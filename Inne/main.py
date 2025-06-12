import matplotlib.pyplot as plt
import numpy as np
import math



def V(t, V0, EL, I0, tau_m):
    return (V0 - EL - I0) * np.exp(-t / tau_m) + EL + I0
    


def Simulate(Vt, T):
    V0 = -70
    EL = -72
    I0 = 4
    tau_m = 15
    
    t = 0 
    
    while t < 400: 
        Vt.append(V(t, V0, EL, I0, tau_m))
        T.append(t)
        
        t += 0.1
        
        
Vt = []
T = []
Simulate(Vt, T)

plt.plot(T, Vt)
plt.show()
