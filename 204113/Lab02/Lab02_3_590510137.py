#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 02
# Problem 3
# 204113 Sec 001

def main():
    a = "11"
    b = "0000"
    plus = False
    length = 2
    print(calculate(a,b,plus,length))

def calculate(a,b,plus,length):
    max_ = max(len(a),len(b))
    a = a.zfill(max_)
    b = b.zfill(max_)


    ## check plus ##
    if plus == False:
        ## two complement b ##
        ls_b = list(b)
        try:
            ## find index of the right one ##
            for i in range (len(ls_b)):
                if ls_b[i] == "1":
                    index_one_right = i
                
            ls_b_2 = ls_b[:index_one_right+1]
            ls_fill_one = list(ls_b_2[index_one_right])

            ## convert left 0f list ##
            for index,num in enumerate(ls_b_2):
                if num == "1":
                    ls_b_2[index] = "0"
                else:
                    ls_b_2[index] = "1"
            
            ls_fill_front = ls_b_2[:index_one_right]
            ls_fill_last = ls_b[index_one_right+1:]
            ls_ = ls_fill_front[:] + ls_fill_one + ls_fill_last[:]
            b = "".join(ls_)
            
        except UnboundLocalError:
            ls_ans = []
            for i in range (len(ls_b)):
                ls_ans.append("0")
            b = "".join(ls_ans)

    else:
        b = b
    
    
    ## plus ##
    result = ""
    add = 0
    for i in range (max_-1,-1,-1):
        r = add
        if a[i] == "1":
            r += 1
        else:
            r += 0
        if b[i] == "1":
            r += 1
        else:
            r += 0
        
        ## check add ##
        if r < 2:
            add = 0
        else:
            add = 1
        
        if r % 2 == 1:
            result = "1" + result
        else:
            result = "0" + result

    if add != 0:
        result = "1" + result
    
    result = result.zfill(max_)



    ls_result = list(result)
    ## cut ##
    if length < len(result) :
        front = len(result) - length
        ls_result = ls_result[front:]
    

    ## binary to decimal ##
    sum_ = 0
    add = 0
    ## check the first ls_str if 1 front of all that is negative##
    if ls_result[0] == "1":
        add = (-1)*(2**(len(ls_result)-1))
        ls_result.pop(0)
    
    ## calculate ##
    for i in range (len(ls_result)):
        sum_ += int(ls_result[i])*(2**(len(ls_result)-(i+1)))
    
    ## plus the first ls_str ##
    sum_ = sum_ + add

    return sum_

if __name__ == "__main__":
    main()