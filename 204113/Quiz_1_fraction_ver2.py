class Fraction (object):
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def print(self):
        if self.denominator == 1:
            print(self.numerator)
        elif self.denominator == 0 :
            print("make it happened")
        else:
            print("{0}/{1}".format(self.numerator, self.denominator))
        

    def reduce(self):
        def gcd(a,b):
            while b:
                a, b = b, a%b
            return a
        gcd = gcd(self.numerator, self.denominator)
        self.numerator = self.numerator//gcd
        self.denominator = self.denominator//gcd

    def add(self, frac):
        if self.denominator > 0 and frac.denominator > 0:
            self.numerator = (self.numerator * frac.denominator) + (frac.numerator * self.denominator)
            self.denominator = self.denominator * frac.denominator
            self.reduce()
        else:
            return None
        return self

    def print_mixed(self):
        self.reduce()
        if self.denominator < self.numerator:
            divide = self.numerator % self.denominator
            print("{0}, {1}/{2}".format((self.numerator//self.denominator), divide, self.denominator))
        else:
            self.print()




def main():
    a = Fraction(-2,10)
    b = Fraction(-10,5)
    a.add(b)
    a.print()

if __name__ == "__main__":
    main()
        