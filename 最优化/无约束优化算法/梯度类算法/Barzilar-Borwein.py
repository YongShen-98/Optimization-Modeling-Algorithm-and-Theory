from target import target, target_grad_x, target_grad_y
import matplotlib.pyplot as plt

alpha = 0.085

def calculate(x1,x2):
    s=[0,0]
    y = [0,0]
    s[0] = x1[len(x1)-1] - x1[len(x1)-2]
    s[1] = x2[len(x2)-1] - x2[len(x2)-2]
    y[0] =  target_grad_x(x1[len(x1)-1],x2[len(x1)-1])-target_grad_x(x1[len(x1)-2],x2[len(x1)-2])
    y[1] =  target_grad_y(x2[len(x2)-1],x2[len(x2)-1])-target_grad_y(x2[len(x2)-2],x2[len(x2)-2])
    return (s[0]*s[0]+s[1]*s[1])/(s[0]*y[0]+s[1]*y[1])

X = []
Y = []
x = -10
y = -1
X.append(x)
Y.append(y)

for i in range(15):
    x = x - alpha*target_grad_x(x,y)
    y = y - alpha*target_grad_y(x,y)
    X.append(x)
    Y.append(y)
    alpha = calculate(X,Y)

plt.plot(X,Y)
plt.scatter(X,Y, s=10)
plt.xlim(-10,10)
plt.ylim(-4,4)
plt.show()