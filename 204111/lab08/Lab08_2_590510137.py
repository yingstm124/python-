#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 08
#problem 2
#204111 Sec 003


def main():
    n = int(input())
    num = int(input())
    print(n_base_to_10(n, num))

def n_base_to_10 (n,num):
    ## base case = base**0 * num
    if num < 10:
        return num  
    else:
        numb = (num%10)
        return numb+(n_base_to_10 (n,num//10)*n)

if __name__ == '__main__':
    main()

