import math
import random
import matplotlib.pyplot as plt
import numpy as np


W = 750

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def generate_astrocytes():
    astr = []

    for i in range(15):
        while True:
            x = random.randint(0, W)
            y = random.randint(0, W)

            flag = True
            for a in astr:
                if dist((x, y), a) < 30:
                    flag = False
                    break

            if flag:
                astr.append((x, y))
                break

    return astr


def generate_neurons():
    neur = []

    for i in range(150):
        while True:
            x = random.randint(0, W)
            y = random.randint(0, W)

            flag = True
            for n in neur:
                if dist((x,y), n) < 30:
                    flag = False
                    break

            if flag:
                neur.append((x, y))
                break

    return neur

def connect_astrocytes(astr):
    astr_connections = set()

    for a1 in astr:
        for a2 in astr:
            if(dist(a1, a2)) < 100:
                if a1 != a2:
                    astr_connections.add((a1, a2))
    '''
    for i in range(len(astr)):
        for j in range(i + 1,len(astr)):
            print(i, j)
            if dist(astr[i], astr[j]) < 100:
                print(astr[i], astr[j])
                astr_connections.add((astr[i], astr[j]))


    '''
    #print(astr_connections)
    return list(astr_connections)



random.seed(0)

astrocytes = generate_astrocytes()
astrocytes_connections = connect_astrocytes(astrocytes)


for a in astrocytes:
    plt.plot(a[0], a[1], 'r^')

neurons = generate_neurons()

for n in neurons:
    plt.plot(n[0], n[1], 'go')



plt.xlabel('x')
plt.ylabel('y')
print(astrocytes_connections[0], astrocytes_connections[1])
#plt.plot(, '-r')
plt.plot([97,75], [633, 700])

plt.show()


