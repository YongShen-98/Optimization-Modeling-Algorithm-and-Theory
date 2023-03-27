import math
def target(x,y):
    return math.pow(x,2)+10*math.pow(y,2)

def target_grad_x(x,y):
    return 2*x

def target_grad_y(x,y):
    return 20*y

