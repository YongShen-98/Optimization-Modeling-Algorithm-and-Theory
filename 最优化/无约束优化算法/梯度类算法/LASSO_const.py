import numpy as np
import scipy as spy
import math

m = 12
n = 24
r = 0.1
A = np.random.random((m,n))
u = spy.sparse.rand(n,1,r,'csc')
u=u.todense()

mu_end = 0.001
mu = 1
delta = 10**(-3)*mu
b = np.dot(A,u)
alpha = 0.001

x = np.random.random((n,1))
