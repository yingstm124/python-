#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 2
# 204111 Sec 003
from math import sqrt 
def main():
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    print(is_p_triple(a,b,c))

    
def is_p_triple(a,b,c):
    if c**2 == (a**2)+(b**2) or c**2 == abs((a**2)-(b**2)):
        return True
    else:
        return False

    return

if __name__=="__main__":
    main()
    
