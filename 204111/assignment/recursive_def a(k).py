### find the a(k) assingment 5 no 2

def a(k):
    if k == 1:
        return 2
    else:
        num = 2*k
        return a(k-1)+num

k = int(input("enter k : "))
print(a(k))
