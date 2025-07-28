import numpy as np
import random

def P(EV, options, a):
    gamma = 10
    sumOpt = 0
    
    for j in options:
        sumOpt += np.exp(gamma * EV[j])
        
    return np.exp(gamma * EV[a]) / sumOpt
        

def UpdateEV(EV, i, r):
    alpha = 0.25
    EV[i] = EV[i] + alpha * (r - EV[i]) 
    
    
def rT(i):
    if random.random() > 0.6:
        return 1
    else:
        return 0
    
    
EV = [0, 0]

print(EV)

for i in range(10):
    index = random.choices([0, 1], [P(EV, [0, 1], 0), P(EV, [0, 1], 1)], k=1)[0]
    UpdateEV(EV, index, rT(index))
    
    print(EV)

print("\n")
    
print('{:f}'.format(P(EV, [0, 1], 0)))
print('{:f}'.format(P(EV, [0, 1], 1)))
