#和LASSO_0对照的看，可以发现用书上提到的从一个较大的alpha开始计算这种方法确实能够降低迭代的步骤。
import numpy as np
from numpy import *
from LASSO_const import m,n,r,A,u,mu,b,x,alpha,delta, mu_end
import matplotlib.pyplot as plt
from time import time,sleep
from tqdm import tqdm
import math


def calculategradL(x, delta):
    gradL = []
    for i in range(len(x)):
        if abs(x[i]) > delta:
            gradL.append(np.sign(x[i]))
        else: gradL.append(x[i]/delta)
    return np.array(gradL)

def calculategradf(x, mu, delta, A, b):
    B =  np.dot(np.transpose(A),A)
    return np.dot(B,x)-np.dot(np.transpose(A),b)+ mu * calculategradL(x, delta)

def calculate(x_k1,x_k2,mu, delta,A, b):
    result1 =  np.dot(np.transpose(x_k2-x_k1),(calculategradf(x_k2,mu,delta, A, b)-calculategradf(x_k1,mu, delta,A, b)))
    result2 = np.dot(np.transpose(calculategradf(x_k2,mu, delta,A, b)-calculategradf(x_k1,mu, delta,A, b)),calculategradf(x_k2,mu,delta, A, b)-calculategradf(x_k1,mu,delta, A, b))
    return result1/result2

def normal(x):
    j = 0
    for i in range(len(x)):
        j += (x[i][0])*(x[i][0])
    return math.sqrt(j)

result_gradf = np.empty(1)
result_x = np.empty(1)
t = 1
while mu > mu_end:
    while normal(calculategradf(x,mu, delta,A,b)) > 10**(-1-t):
        xnew = x - alpha*calculategradf(x, mu, delta, A, b)
        xnew = xnew.getA()                                       ##把计算出来的数据从matrix转换成array
        alpha = calculate(x, xnew, mu, delta, A, b)
        alpha=mat(alpha[0])[0,0]                                 ##把计算出来的alpha从matrix转换成数值
        x = xnew
        result_gradf = np.append(result_gradf,normal(calculategradf(x,mu, delta,A,b)))
    if normal(calculategradf(x,mu, delta,A,b)) < 10**(-6):
        break
    t+=1
    mu = 0.1*mu
    delta = mu*10**(-3)
print(len(result_gradf))


    




