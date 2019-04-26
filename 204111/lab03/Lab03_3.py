#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 03
# Problem 3
# 204111 Sec 003

def main():
    #รับค่า x1
    x1 = float(input(""))
    octa1 = octagon_area(x1)
    #แสดงค่าocta1จากฟังก์ชั่น octagon(x1)
    print("%.6f"%octa1)

def triangle_area(x):
    area = abs(0.5*(x/3)*(x/3))
    return area

def squere_area(x):
    area = abs(x*x)
    return area

def octagon_area(x):
    area = (squere_area(x))-(4*(triangle_area(x)))
    return area

if __name__=="__main__":
    main()
    
