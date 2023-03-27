from target import params, target, x, target_grad

alpha = params["alpha"]
c = params["c"]
c_1 = params["c_1"]
gamma = params["gamma"]
c_2 = params["c_2"]
d = params["d"]

while target(x[1000]+alpha*d) > target(x[1000]) + c_1*alpha*target_grad(x[1000])*d :
    alpha = gamma*alpha
print(alpha)

while target(x[1000]+alpha*d) > target(x[1000]) + (1-c)*alpha*target_grad(x[1000])*d:
    alpha = alpha-0.1
print(alpha)
