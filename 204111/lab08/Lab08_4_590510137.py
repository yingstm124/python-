#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 08
#problem 4s
#204111 Sec 003

def main():
    n = int(input())
    print(series(n))


def series(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (2**(n-1))+series(n-2)

if __name__ == '__main__':
    main()

