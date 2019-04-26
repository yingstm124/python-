def main():
    a = "1101"
    b = "01000"
    plus = True
    length = 5
    print(calculate(a,b,plus,length))

def binary_to_decimal(str_binary):
    ls_result = list(str_binary)
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
    
    #print("decimal is {0}".format(sum_))

    return sum_

def two_complement(x):
    ## str x ##
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

        
    except UnboundLocalError:
        ls_ans = []
        for i in range (len(ls_str)):
            ls_ans.append("0")
        ans = "".join(ls_ans)
        binary  = ans 
        return binary 

    return binary

def overflow(str_answer,length):
    new_str = ""
    for i in range (-1,-length-1,-1):
        new_str = str_answer[i]+new_str

    return new_str

def add(str_a,str_b,length):  
    str_answer = ""
    add = 0
    for i in range (length-1,-1,-1):
        result = add
        ## check value of str_a ##
        if str_a[i] == "1":
            result += 1
        elif str_a[i] == "0":
            result += 0 
        ## check value of str_b ##
        if str_b[i] == "1":
            result +=  1 
        elif str_b[i] == "0":
            result += 0
        
        ## process answer ##
        if result % 2 == 1:
            str_answer = "1" + str_answer
        else:
            str_answer = "0" + str_answer

        ## check add after process ##
        if result < 2 :
            add = 0
        else:
            add = 1

    if add == 1 :
        str_answer = "1" + str_answer 
    

    return str_answer
        
def limit_length(str_a,str_b,length,max_len,min_len):

    for i in range (abs(length-min_len)):
        if len(str_a) < max_len:
            if str_a[0] == "1":
                str_a = "1" + str_a
            else:
                str_a = "0" + str_a

        if len(str_b) < max_len:
            if str_b[0] == "1":
                str_b = "1" + str_b
            else:
                str_b = "0" + str_b

    return str_a,str_b

def calculate(a,b,plus,length):
    max_ = max(len(a),len(b))
    min_ = min(len(a),len(b))
    ## trap ##
    if length < max_:
        return None

    ##limit of length ##
    a , b = limit_length(a,b,length,max_,min_)
    #print(a)
    #print(b)

    ## check plus ##
    if plus == False:
        ## two complement b##
        b =  two_complement(b)
        #print(b)

    ## add ##
    str_answer = add(a,b,length)
    #print(str_answer)

    ## overflow ##
    new_str_answer = overflow(str_answer,length)
    #print(new_str_answer)

    ## binary to decimal ##
    answer_decimal = binary_to_decimal(new_str_answer)
    #print(answer_decimal)

    return answer_decimal

if __name__ == "__main__":
    main()

