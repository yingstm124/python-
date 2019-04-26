#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 03
# Problem 5
# 204111 Sec 003

def main():
    # รับค่า number1 
    number1 = int(input(""))
    # รับค่าหลักk1ที่ต้องการ
    k1 = int(input(""))
    # รับค่าเลขที่ไปแทนที่ในหลักk1ที่number1
    value1 = int(input(""))
    kth1 = set_kth_digit(number1,k1,value1)
    # แสดงค่าkth1 ใน set_kth_digit function
    print(kth1)

def kth_digit(number,k):
    number = abs(number)%(10**(k+1))
    reminder = number//(10**k)
    kth = reminder
    return kth

def set_kth_digit(number,k,value):
    a = kth_digit(number,k)
    b = a*(10**k)
    c = number-b
    d = value*(10**k)
    result = c+d
    return result

if __name__=="__main__":
    main()
    
    
