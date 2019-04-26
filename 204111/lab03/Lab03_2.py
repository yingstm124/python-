#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 03
# Problem 2
# 204111 Sec 003

def main():
    # รับค่าx1 
    x1 = int(input(""))
    rev1 = reverse_digits(x1)
    # แสดงrev1ใน reverse_digits function
    print(rev1)
    
def reverse_digits(x):
    x = abs(x)
    x1 = x%10
    x2 = (x%100)-x1
    x3 = (x%1000)-x2
    x4 = (x%10000)-x3

    x11 = x1*1000
    x12 = x2*10
    x13 = x3//10
    x14 = x4//1000

    rev = x11+x12+x13+x14

    return rev

if __name__=="__main__":
    main()
