#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 08
#problem 1
#204111 Sec 003

def main():
    x = int(input())
    y = int(input())
    print(gcd(x, y))

def gcd(x, y):

    if y == 0:
        return x
    else:
        return gcd(y ,x%y)


if __name__=="__main__":
    main()


