import numpy as np
import matplotlib.pyplot as plt


def radius(x):
    return np.dot(x,x)


n = 10000
vol = []
for d in range(1,11): 
    accept = 0
    total = 0
    while accept<n:
        a = np.random.rand(d)*2-1
        if radius(a)<1: accept +=1
        total +=1
    volume = (n/total)*(2**d)
    print(f'Volume of a {d} dimensional sphere is {volume}')
    vol.append(volume)


plt.plot(range(1,11),vol, label = 'Volume of n-dimensional unit sphere')
plt.title('n-sphere')
plt.xlabel('Dimension')
plt.ylabel('Volume')
plt.legend()
plt.grid()
plt.show()

