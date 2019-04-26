#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 1
# 204113 Sec 001

import math

def main():
    n = input()
    n = n.split()
    
    if n[0] == "c":
        c = Circle(float(n[1]))
        c.print()
    elif n[0] == "r":
        r = Rectangle(float(n[1]),float(n[2]))
        r.print()


class Circle(object):
    # constructure
    def __init__(self , r):
        self.radius = abs(r)
    # perimeter method
    def perimeter(self):
        return 2 * math.pi * self.radius
    # area method
    def area(self):
        return math.pi * (self.radius**2)
    # print method
    def print(self):
        print("Circle perimeter is {0:.2f}".format(self.perimeter()))
        print("Circle area is {0:.2f}".format(self.area()))

class Rectangle(object):
    # constructure
    def __init__(self , w , h):
        self.wide = abs(w)
        self.hight = abs(h)
    # perimeter method
    def perimeter(self):
        return (2*self.wide)+(2*self.hight)
    # area method
    def area(self):
        return self.wide * self.hight
    # print method
    def print(self):
        print("Rectangle perimeter is {0:.2f}".format(self.perimeter()))
        print("Rectangle area is {0:.2f}".format(self.area()))



if __name__ == "__main__":
    main()


