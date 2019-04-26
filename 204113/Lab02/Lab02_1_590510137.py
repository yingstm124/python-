#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 02
# Problem 1
# 204113 Sec 001

def main():
    x = input("")
    ## test in loop ##
    for i in x:
        if i == "0" or i == "1":
            check = True
        else:
            check = False
            break
    if check == True:
        print(string_to_signed_int(x))
    else:
        print("error")

def string_to_signed_int(str_):
    ls_str = list(str_)
    result = 0
    plus = 0

    ## check the first ls_str if 1 front of all that is negative##
    if ls_str[0] == "1":
        plus = (-1)*(2**(len(ls_str)-1))
        ls_str.pop(0)
    
    ## calculate ##
    for i in range (len(ls_str)):
        result += int(ls_str[i])*(2**(len(ls_str)-(i+1)))
    
    ## plus the first ls_str ##
    result = result + plus
        
    return  result


if __name__ == "__main__":
    assert 11 == string_to_signed_int("1011")
    

