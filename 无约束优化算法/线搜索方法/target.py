import math
x=[]
for i in range(-1000,1000):
    x.append(i/10)

def target(x):
    return math.pow(x-2,2)

def target_grad(x):
    return (target(x+0.00001)-target(x))/(0.00001)
params = {
    "alpha": 10,
    "c_1": 0.001,
    "c": 1/4,
    "gamma": 0.5,
    "c_2": 0.9,
    "d": 1
}
 


