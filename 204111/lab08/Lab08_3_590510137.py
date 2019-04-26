#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 08
#problem 3
#204111 Sec 003

def main():
    n = int(input())
    print(is_prime(n))

def is_prime(n,i = 2):
    ### lower 2 is a prime except only 2 ###
    if n == 2 :
        return True

    ### have a other num can divide  ###
    if n%i == 0:
        return False

    ## extent of i not more sqrt(n) ###
    if i > (n**0.5):
        return True

    ##  i++1  ####
    return is_prime(n,i+1)

if __name__ == '__main__':
    main()
