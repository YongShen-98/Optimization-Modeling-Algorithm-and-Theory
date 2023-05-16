from constant import *
import numpy as np
import matplotlib.pyplot as plt
from target import target, grad_target, ggrad_target, sum  
import math

def Cholesky(A):
    D = np.eye(A.shape[0])
    L = np.eye(A.shape[0])
    for j in range(A.shape[0]):
        if j == 0:
            D[0][0] = A[0][0]
            for i in range(1, A.shape[0]):
                L[i][0]=A[i][j]/D[j][j]
        else:
            r = 0
            for s in range(j-1):
                r+=D[s][s]*L[j][s]*L[j][s]
            c = A[j][j] - r
            D[j][j] = c
            for i in range(j+1, A.shape[0]):
                r = 0
                for s in range(j-1):
                    r+=D[s][s]*L[i][s]*L[j][s]
                c = A[i][j] - r
                L[i][j] = c/D[j][j]
    return L,D

def solve(A, b):
    Y = np.zeros(A.shape[0])
    for n in range(A.shape[0]):
        if n == 0:
            Y[0] = b[0]
        for i in range(n-1):
            b[n] -= A[n][i]*Y[i]
        Y[n] = b[n]/A[n][n]
    return Y

def norm(x):
    r = 0
    for i in range(len(x)):
        r += x[i]*x[i]
    return math.sqrt(r)

def Newton(step, x):
    result=[]
    for k in range(step):
        L,D =Cholesky(ggrad_target(x))
        Y = solve(L, -grad_target(x))
        d = solve(D@np.transpose(L), Y)
        alpha = 1
        x_next = sum(x,alpha*d)
        result_re = target(x)
        result_be= target(x_next)
        r=0
        while result_be > result_re+r:
            alpha = alpha*0.5
            x_next = sum(x,alpha*d)
            result_be = target(x_next)
            r = grad_target(x)@d*alpha*0.001
        x = x_next
        result.append(norm(grad_target(x)))
    return result

if __name__ == '__main__':
    x = np.random.random(n)

    result = Newton(10,x)
    plt.plot(range(10),result)
    plt.show()
