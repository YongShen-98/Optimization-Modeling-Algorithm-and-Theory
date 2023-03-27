import numpy as np
import scipy as spy
import math

m = 2
n = 1
r = 0.1
A = np.random.random((m,n))
b = np.random.random((n,1))
ttt = np.empty(1)
x = np.random.random((n,1))
#print(np.append(m,1))

def normal(x):
    j = 0
    for i in range(len(x)):
        j += (x[i])*(x[i])
    return math.sqrt(j)

np.transpose(A@x-b)@(A@x-b)
#print(np.zeros(10))
a = np.array([1])
b = np.array([2])
a = np.random.random(5)
b = np.random.random(5)
for s in range(1):
    print(s)


