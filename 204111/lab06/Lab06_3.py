#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 3
# 204111 Sec 003

from math import sqrt

def main():
    x = int(input())
    factorize(x)

def factorize(x):
    i = 2
    y = True
    print("%d is "%x,end="")

    while i<= (x)**0.5:
        if x%i == 0:
            x = int(x/i)
            y = False
            print(i,end=" * ")
        else :
            i+=1
            
    if y == False:
        print(x)
    else:
        print("prime")
           
  

main()
        
