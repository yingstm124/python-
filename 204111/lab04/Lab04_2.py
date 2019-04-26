#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 2
# 204111 Sec 003

def main():
    a1 = int(input(""))
    b1 = int(input(""))
    c1 = int(input(""))
    result1 = my_max_mid_min(a1,b1,c1)



def my_max_mid_min(a,b,c):
    
    if a>b:
        max_ = a
        min_ = b
    else:
        max_ = b
        min_ = a

    mid_ = c
    if c>max_ :
        mid_ = max_
        max_ = c
    if c<min_:
        mid_ = min_
        min_ = c
    print ("max = %d\nmid = %d\nmin = %d"%(max_,mid_,min_))
    
if __name__=="__main__":
    main()
