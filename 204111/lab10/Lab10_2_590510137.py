#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 10
#problem 2
#204111 Sec 003

def main():
    x = int(input())
    b = int(input())
    print(is_palindrome (x,b))

def is_palindrome (x,b):
    new_number = decimal_to_base (x,b)
    ## convert to list type str ###
    list_str_newnum = list(str(new_number))
    list_str_newnum.reverse()
    ## convert take off list of new_num ###
    without_list = int("".join(map(str,list_str_newnum)))

    if without_list == new_number :
        return True
    else:
        return False


def decimal_to_base (number,base):
    i = 0
    sum_ = 0
    while number > 0:
        mod = number%base
        num = number//base
        sum_ += mod*(10**i)
        i += 1
        number//=base

    return sum_


if __name__ == '__main__':
    main()

