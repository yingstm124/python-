import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

def plot(ls):
    color = "#00802B"
    a = 12
    x = [i for i in range (len(ls))]
    plt.scatter(x, ls, s=a, c=color, alpha=0.5)
    plt.xlabel("x")
    plt.show()
    

def rand(n):
    x = (int)(time.time())
    y = datetime.datetime.now()
    m = (int)(y.microsecond)
    a = (int)(y.minute + y.second)
    c = (int)(y.minute)
  
    result = []

    seed = x
    print(x,m,a,c)
    print()
    for i in range (n):
        xi = (a*x + c) % m
        result.append(xi/m)
        x = xi

    return result


ls = rand(100)
plot(ls)
