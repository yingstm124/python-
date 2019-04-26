### assignment 5 no.3
def digitsum(x):
    sum_ = 0
    if x<1:
        return x%10
    else:
        mod = x%10
        sum_ += mod

        return sum_+digitsum(x//10)

x = int(input("enter x : "))
print(digitsum(x))
