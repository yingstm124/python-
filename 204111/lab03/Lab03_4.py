#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 03
# Problem 4
# 204111 Sec 003

def main():
    #รับค่าจำนวนเต็ม4หลัก
    number1 = int(input(""))
    #รับค่าหลักที่ต้องการ
    k1 = int(input(""))
    #แสดงข้อมูลใน kth_digit function 
    kth1 = kth_digit(number1,k1)
    print(kth1)

def kth_digit(number,k):
    number = abs(number)%(10**(k+1))
    reminder = number//(10**k)
    kth = reminder
    return kth

if __name__=="__main__":
    main()
          
