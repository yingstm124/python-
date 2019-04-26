def main():
    n = int(input(""))
    fibonacci(n)

def fibonacci(n):
    ## set begining value ##
    f1 = 0
    f2 = 1
    sum_ = 0
    ## print 0 if input value is 0 ##
    if n == 0:
        print(0)
    ## 0,...... for value get 1 up ## 
    elif n > 0:
        print(0,end=",")
    ## loop 0,1,............. in range of input value ##
    for i in range (n):
        f1 = sum_
        sum_ = f1+f2
        f2 = f1
        ## limit for , ##
        if i == (n-1):
            print(sum_,end="")
        else:
            print(sum_,end=",")



if __name__ == "__main__":
    main()