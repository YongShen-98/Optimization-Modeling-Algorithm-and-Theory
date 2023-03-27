import math
from constant import *

def sum(x,y):
    r = np.zeros(n)
    for i in range(len(x)):
        r[i] = x[i]+y[i]
    return r

def target(x):
    result = 0
    for i in range(m):
        result+= math.log(1+math.exp(-b[i]*(A[i,:]@x)),math.e)
    return (1/m)*result+Lambda*(np.transpose(x)@x)

def p(x):
    p = np.zeros(m)
    for i in range(m):
        p[i] = 1/(1+math.exp(-b[i]*(A[i,:]@x)))
    return p

def grad_target(x):
    a = -(1/m)*np.transpose(A)@(b-np.transpose(b)@p(x))
    return sum(a,x)

def w(x):
    w = np.eye(m)
    for i in range(m):
        w[i,i] = p(x)[i]*(1-p(x)[i])
    return w

def ggrad_target(x):
    return (1/m)*np.transpose(A)@w(x)@A+2*Lambda*np.eye(n)

if __name__ == '__main__':
    x = np.random.random(n)
    print(ggrad_target(x))
    print(np.transpose(ggrad_target(x)))
    print(ggrad_target(x)==np.transpose(ggrad_target(x)))