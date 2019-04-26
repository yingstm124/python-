#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 12
#problem 3
#204111 Sec 003

def main():
    a = 180
    b = 48
    print(coprime_factor(a, b))


def prime_factor(n):

    lst_prime = []

    divide = 2
    while divide <= (n**0.5):
        if n % divide == 0:
            lst_prime.append(divide)
            n //= divide
        else:
            divide += 1
    if n != 1:
        lst_prime.append(n)


    return lst_prime


def coprime_factor(a, b):
    lst_a_prime = prime_factor(a)
    lst_b_prime = prime_factor(b)

    lst_co = []

    for i in lst_a_prime:
        for j in range (len(lst_b_prime)):
            if lst_b_prime[j] == i :
                lst_co.append(i)
                lst_b_prime.remove(lst_b_prime[j])
                break

    return lst_co


if __name__ == '__main__':
    main()




