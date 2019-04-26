def main():
    a = "1101"
    b = "01000"
    plus = True
    length = 4
    print(calculate(a,b,plus,length))

def calculate(a,b,plus,length):
   ## limit length a ##
    if length > len(a):
        for i in range (length-len(a)):
            if a[0] == "1":
                a = "1" + a
            elif a[0] == "0":
                a = "0" + a
    else:
        new_a = ""
        for i in range (-1,(-1)*length-1,-1):
            new_a = a[i] + new_a
        a = new_a

    ## limit length b #
    if length > len(b):
        for i in range (length-len(b)):
            if b[0] == "1":
                b = "1" + b
            elif b[0] == "0":
                b = "0" + b
    else:
        new_b = ""
        for i in range (-1,(-1)*length-1,-1):
            new_b = b[i] + new_b
        b = new_b

    # print("a is {0}".format(a))
    # print("b is {0}".format(b))

    ## check plus ##
    if plus == False:
        ## two complement ##
        b = two_complement(b)
        #print("b two com is {0}".format(b))
    else:
        b = b
    
    ## plus ##
    add = 0
    result = ""
    for i in range (length-1,-1,-1):
        r = add
        if a[i] == "1":
            r += 1
        else:
            r += 0
        
        if b[i] == "1":
            r += 1
        else:
            r += 0
        
        ## check result ##
        if r % 2 == 1 :
            result = "1" + result
        else:
            result = "0" + result
        
        ## check add ##
        if r < 2:
            add = 0
        else:
            add = 1
    
    if add != 0:
        result = "1" + result

    #print("result after plus process is {0}".format(result))

    ## overflow ##
    answer_str = ""
    for i in range (-1,(-1)*(length)-1,-1):
        answer_str = result[i] + answer_str

    #print("answer is {0}".format(answer_str))
    
    ## binary to decimal ##
    answer_str = binary_to_decimal(answer_str)

    #print("decimal {0}".format(answer_str))

    return answer_str


def two_complement(str_):
    ## find the right index ##
    try:
        for i in range (len(str_)):
            if str_[i] == "1":
                index_right = i

        right_str = str_[index_right:]
        left_str = str_[:index_right]
        ## converse 1 to 0 ##
        converse_str = ""
        for i in left_str:
            if i == "1":
                converse_str += "0"
            else:
                converse_str += "1"

        result = converse_str + right_str
    except UnboundLocalError:
        return str_

    return result

def binary_to_decimal(str_):
    ls_result = list(str_)
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

    # print(calculate('00100', '00100', True, 5))
    # print(calculate('0101', '01000', True, 5))
    # print(calculate('0101', '1000', True, 4))
    # print(calculate('1101', '100', False, 5))
    # print(calculate('101', '1110', False, 10))
    # print(calculate('1010', '11', True, 4))
    # print(calculate('001', '110', False, 3))
    # print(calculate('001', '010', False, 4))
    # print(calculate('000', '000', True, 4))
