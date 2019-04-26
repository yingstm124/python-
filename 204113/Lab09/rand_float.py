#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 09
# Problem 1
# 204113 Sec 001

import numpy as np
import matplotlib.pyplot as plt
import time
import datetime
import random

def seed():

    x = int(time.time())
    now = datetime.datetime.now()
    m = int(now.microsecond)
    a = int(now.minute + now.microsecond)
    c = int(now.minute)
    
    return x, m, a, c

def rand_float():
    n = random.randint(0,10000)
    x, m, a, c = seed()
    
    result = []
    for i in range (n):
        xi = (a*x + c) % m
        result.append(xi/m)
        x = xi

    return result

def plot(result_ls):
    color = "Red"
    area = 18
    x = [i for i in range (len(result_ls))]
    plt.scatter(x, result_ls, s=area, c=color, alpha=0.5)
    plt.xlabel("x")
    plt.show()


def main():
    result = rand_float() 
    plot(result)
    


if __name__ == "__main__":
    main()
