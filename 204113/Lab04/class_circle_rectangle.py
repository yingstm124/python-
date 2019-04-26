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
    def __init__(self , r):
        self.radius = abs(r)
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * (self.radius**2)
    def print(self):
        print("Circle perimeter is {0:.2f}".format(self.perimeter()))
        print("Circle area is {0:.2f}".format(self.area()))

class Rectangle(object):
    def __init__(self , w , h):
        self.wide = abs(w)
        self.hight = abs(h)
    def perimeter(self):
        return (2*self.wide)+(2*self.hight)
    def area(self):
        return self.wide * self.hight
    def print(self):
        print("Rectangle perimeter is {0:.2f}".format(self.perimeter()))
        print("Rectangle area is {0:.2f}".format(self.area()))



if __name__ == "__main__":
    main()


