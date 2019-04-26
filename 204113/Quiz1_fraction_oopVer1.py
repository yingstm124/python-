import copy

class Fraction (object):
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d

    def print(self):
        if self.numerator == 0 or self.denominator == 1:
            print(self.numerator)
        elif self.denominator == 0:
            print("Division by 0 None/None")
        else:
            print("{0}/{1}".format(self.numerator,self.denominator))
    
    def prime_factor(self,num):
        i = 2
        ls = []
        while num*num > i :
            if i == 2 or num%2 != 0:
                if num%i == 0:
                    ls.append(i)
                    num = num//i
                else:
                    i += 1
            else:
                i += 1
        return ls
    
    def check_prime(self, num_1, num_2):
        if num_1 == 2 or num_2 == 2 or num_1 % num_2 != 0:
            return True
        else:
            return False

    def reduce(self):
        if self.numerator != self.denominator:
            ls_n = self.prime_factor(self.numerator)
            ls_d = self.prime_factor(self.denominator)

            if len(ls_n) > len(ls_d):
                max_ = ls_n
                min_ = ls_d
                switch = True
                i = 0
                check = True
                if self.denominator > self.numerator:
                    while check == True and i < len(max_):
                        check = self.check_prime(max_[i],self.denominator)
                        i += 1
            else:
                max_ = ls_d
                min_ = ls_n
                switch = False
                i = 0
                check = True
                if self.denominator > self.numerator:
                    while check == True and i < len(max_):
                        check = self.check_prime(max_[i],self.numerator)
                        i += 1
                
            # loop
            min_copy = copy.deepcopy(min_)
            if check == True:    
                i = 0
                while i < len(min_):
                    if min_[i] in max_:
                        max_.remove(min_[i])
                        min_copy.remove(min_[i])
                    i += 1                    
            
            if switch == True:
                ls_n = max_
                ls_d = min_copy
            else:
                ls_n = min_copy
                ls_d = max_
                
            if ls_n == []:
                ls_n.append(1)
            if ls_d == []:
                ls_d.append(1)

            # checking negative number
            nega = False
            if self.numerator < 0 or self.denominator < 0:
                nega = True
            if self.numerator < 0 and self.denominator < 0:
                nega = False

            multi = 1
            for i in range (len(ls_n)):
                multi *= ls_n[i]
            self.numerator = multi

            multi = 1
            for i in range (len(ls_d)):
                multi *= ls_d[i]
            self.denominator = multi

            if nega == True:
                self.numerator = self.numerator * -1
        
        else:
            self.numerator = 1
            self.denominator = 1
    
    def add(self, frac):    
        self.reduce()
        frac.reduce()
        
        if self.denominator != frac.denominator:
            self.numerator = ((self.numerator * frac.denominator)+(frac.numerator * self.denominator))
            self.denominator = (self.denominator * frac.denominator)
        else:
            self.numerator = (self.numerator + frac.numerator)
            self.denominator = frac.denominator

        ans = Fraction(self.numerator, self.denominator)
        ans.reduce()
        return ans
    
    def print_mixed(self):
        self.reduce()
        if self.denominator < self.numerator:
            divide = self.numerator % self.denominator
            print("{0}, {1}/{2}".format((self.numerator//self.denominator), divide, self.denominator))
        else:
            self.print()


def main():
    a = Fraction(4,7) 
    a.print_mixed()

if __name__ == "__main__":
    main()


