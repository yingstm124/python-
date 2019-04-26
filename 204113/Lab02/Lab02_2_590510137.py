#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 02
# Problem 2
# 204113 Sec 001

def main():
    x = input("")
    print(two_complement(x))

def ls_string_to_signed_int(ls_str):
    result = 0
    plus = 0

    ## check front of binary ##
    if ls_str[0] == "1":
        plus = (-1)*(2**(len(ls_str)-1))
        ls_str.pop(0)
    
    ## convert binary to decimal ##
    for i in range (len(ls_str)):
        result += int(ls_str[i])*(2**(len(ls_str)-(i+1)))
    
    ## add front of binary ##
    result = result + plus
        
    return  result

def two_complement(x):
    ls_str = list(x)
    try:
        ## find index of the right one ##
        for i in range (len(ls_str)):
            if ls_str[i] == "1":
                index_one_right = i
            
        ls_str_2 = ls_str[:index_one_right+1]
        ls_fill_one = list(ls_str_2[index_one_right])

        ## convert left 0f list ##
        for index,num in enumerate(ls_str_2):
            if num == "1":
                ls_str_2[index] = "0"
            else:
                ls_str_2[index] = "1"
        
        ls_fill_front = ls_str_2[:index_one_right]
        ls_fill_last = ls_str[index_one_right+1:]
        ls_ = ls_fill_front[:] + ls_fill_one + ls_fill_last[:]
        binary = "".join(ls_)

        ## convert binary to decimal ##
        decimal = ls_string_to_signed_int(ls_)
        
    except UnboundLocalError:
        ls_ans = []
        for i in range (len(ls_str)):
            ls_ans.append("0")
        ans = "".join(ls_ans)
        binary , decimal = ans , 0
        return binary , decimal

    return binary,decimal

 
        

if __name__ == "__main__":
    main()