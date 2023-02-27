from target import target, target_grad_x, target_grad_y
import matplotlib.pyplot as plt
alpha = 0.085

X = []
Y = []
x = 10
y = 1
X.append(x)
Y.append(y)

for i in range(15):
    x = x - alpha*target_grad_x(x,y)
    y = y - alpha*target_grad_y(x,y)
    X.append(x)
    Y.append(y)

plt.plot(X,Y)
plt.scatter(X,Y, s=10)
plt.xlim(-10,10)
plt.ylim(-4,4)
plt.show()