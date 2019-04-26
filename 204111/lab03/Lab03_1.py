#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 03
# Problem 1
# 204111 Sec 003

import math

def sphere_volume(sa):
    r = math.sqrt(abs(sa/(4*math.pi)))
    v = abs((1/3)*sa*r)
    return v
    
def main():
    # รับค่า sa1 (surface_area)
    sa1 = float(input("input surface area: "))
    v1 = sphere_volume(sa1)
    # แสดงค่าv1 ใน sphere_volume function 
    print("volume = %.2f"%v1)
    
if __name__=="__main__":
    main()
    
