import matplotlib.pyplot as plt
import numpy as np
import math

taum = 5
dt = 0.1

def Ix(T):
    np.sin(T)

EL = 70

T = np.arange(-5 * taum, 5 * taum, dt)

k = (1 / taum) * np.exp(-T / taum) * (T > 0)

V = EL + np.convolve(Ix(T), k, mode='same') * dt

plt.plot(T, V)
plt.show()