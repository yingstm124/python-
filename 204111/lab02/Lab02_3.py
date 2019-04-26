#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 02
#problem 3
#204111 Sec 003

print("First Equation")
m1=float(input("Input m1: "))
b1=float(input("Input b1: "))
print("Second Equation")
m2=float(input("Input m2: "))
b2=float(input("Input b2: "))

if(m1!=m2):
    x=(b2-b1)/(m1-m2)
    y=m1*((b2-b1)/(m1-m2))+b1
    print("The point of intersection is at x = %.2f and y = %.2f"%(x,y)) 
else:
    print("not answer")
