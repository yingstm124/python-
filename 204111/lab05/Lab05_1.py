#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 1
# 204111 Sec 003
from math import sqrt

def main():
    x1 = float(input(""))
    y1 = float(input(""))
    r1 = float(input(""))
    x2 = float(input(""))
    y2 = float(input(""))
    r2 = float(input(""))
    result = intersects(x1,y1,r1,x2,y2,r2)
    print(result)


def intersects(x1,y1,r1,x2,y2,r2,epsilon = 10**-6):
    r1 = abs(r1)
    r2 = abs(r2)
    distance = sqrt(((x1-x2)**2)+((y1-y2)**2))

    if abs(distance - (r2+r1)) < epsilon :
      return 0

    elif distance < r1+r2:
      return 1
    
    else:
      return -1
  

if __name__=="__main__":
  main()


