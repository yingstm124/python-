#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 5
# 204111 Sec 003

def main():
    x1 = float(input(""))
    result1 = nearest_odd(x1)
    print(result1)

def nearest_odd(x):
    num = x//1
    modulo = num%2
    if modulo == 0:
        return int(num+1)
    else:
        return int(num)
    
        
if __name__=="__main__":
    main()
    
