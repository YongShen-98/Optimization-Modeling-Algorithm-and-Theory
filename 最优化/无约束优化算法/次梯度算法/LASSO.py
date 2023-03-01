import sys
sys.path.append(r"C:\\Users\\Shen\\Desktop\\最优化\\无约束优化算法\\梯度类算法")
from LASSO_const import *
import matplotlib.pyplot as plt

def subgrandf(x, A, b, mu):
    g = np.transpose(A)@A@x - np.transpose(A)@b
    for i in range(len(x)):
        if x[i]>0:
            g[i] = g[i]+mu
        elif x[i]<0:
            g[i] = g[i]-mu
        elif x[i]==0:
            g[i] = 0
    return g

def result(x):
    return np.transpose(A@x-b)@(A@x-b) + mu*max(x)

mu = 1

alpha =  0.0005
alpha1 = 0.0002
alpha2 = 0.0001
alpha3 = 0.01

x1 = x
x2 = x
x3 = x

for i in range(4000):
    xnew = x - alpha*subgrandf(x,A,b,mu)
    x = xnew
    result_0 = result(x)
    
    xnew1 = x1 - alpha1*subgrandf(x1,A,b,mu)
    x1 = xnew1
    result_1 = result(x1)

    xnew2 = x2 - alpha2*subgrandf(x2,A,b,mu)
    x2 = xnew2
    result_2 = result(x2)

    xnew3 = x3 - alpha3*subgrandf(x3,A,b,mu)
    x3 = xnew3
    alpha3 = 0.01/(i+1)
    result_3 = result(x3)

print(result_0,result_1,result_2,result_3)
