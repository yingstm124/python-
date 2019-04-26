def main():
    n = int(input("Enter n :"))
    print(primecheck(n))

def primecheck(n):
    ## set up prime equal True first ##
    prime = True
    ## loop untill to n-1 for check range of num ##
    for i in range (2,n):
        ## if num is divide get break out of loop & return False ##
        if n%i == 0:
            prime = False
            break

    return prime

if __name__ == "__main__":
    main()
# print(primecheck(1))
# print(primecheck(2))
# print(primecheck(3))
# print(primecheck(7))
# print(primecheck(5))
# print(primecheck(9))