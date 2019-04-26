#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 4
# 204111 Sec 003

def main():
    x1 = float(input(""))
    result1 = round_to_int(x1)
    print(result1)

def round_to_int(x):
    divide = int(abs(x)//1)
    reminder = abs(x)-divide

    if reminder>=0.5:
        result = divide+1
    else:
        result = divide

    if x>0:
        return (result)
    else:
        return (-result)

    return int(result)
    
if __name__=="__main__":
    main()
    
