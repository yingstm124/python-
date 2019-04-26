def main():
    #text = "!!i dog-123,122.654 -a100nd asdf----6.901 h-45-20-1- a,-12nd -1,345.22 ---"
    #text = "-100.33i saw dog a17-42 --60.55cat"
    #text = "I     saw !!-1,279 dogs, -17--- cats, and 14.6786--- cows!"
    #text = "I saw 3 dogs, 17 cats, and 14 cows!"
    #text = ",a,1,002,777.,2223sdf99.22g@-50#%$-a10dfg7hj33." 
    #text = "      12    990.634     -3  100     3.21  1,233.45"
    #text = "qwertyujsd"
    #text = "asf-11,.,m"
    text = "12,3-.,"
    
    print(largest_number(text))

def check_digit_behind(str_):
    if str_[0].isdigit():
        return True
    else:
        return False

def index_identify(key, letter):
    index = 0
    for char in letter:
        if char == key:
            break
        else:
            index += 1

    return index


def largest_number(text):
    text = text.strip(" ")
    text = text.strip(".")
    text = text.rstrip("-")
    text = text.replace("-"," -")

    text_ls = text.split(" ")
    string_ls = ["-", ".", ","]

    #print(text_ls)

    digit_ls = []
    for i in range (len(text_ls)):

        digit = ""
        index = 0
        check_digit = False
        for char in text_ls[i]:
            index += 1
            if char.isdigit() == True:
                check_digit = True
                digit += char
                continue
            
            elif char in string_ls:
                check_last = text_ls[i][index:]
                if char == "-":
                    if check_digit == True:
                        if digit != "" :
                            digit_ls.append(digit)
                        check_digit = False 
                        digit = ""
                    
                if check_last != "" :
                    check = check_digit_behind(check_last)

                    if check == True :
                        digit += char
                        continue
                
                
            elif char.isdigit() == False:
                if digit != "" and check_digit == True :
                    digit_ls.append(digit)
                
                check_digit = False
                digit = ""
            
            if digit != "" :
                    digit_ls.append(digit)
                    check_digit = False
                    digit = ""
                    
        if check_digit == True: 
            if digit != "" :
                    digit_ls.append(digit)

    if digit_ls == []:
        return None

    ls_result = []
    for i in range (len(digit_ls)):
        digit_ls[i] = digit_ls[i].strip(" ")
        digit_ls[i] = digit_ls[i].strip(".")
        digit_ls[i] = digit_ls[i].strip(",")
        digit_ls[i] = digit_ls[i].replace(",","")

        if digit_ls[i].count(",") == 0 and digit_ls[i].count(".") == 0 and digit_ls[i].count("-") == 0:
            result = int(digit_ls[i])

        
        elif digit_ls[i].count(".") == 1:
            index_ = index_identify(".", digit_ls[i])
            front = int(digit_ls[i][:index_]) 
            last = int(digit_ls[i][index_+1:]) * 10**( -1 * len(digit_ls[i][index_+1:]) )
            result = front + last
        
        elif digit_ls[i].count("-") == 1:
            result = -1 * int(digit_ls[i][1:])

        ls_result.append(result)
   

    #print(digit_ls)
    #print(ls_result)

    if ls_result != []:
        max_ = max(ls_result)            
        return  max_
    else:
        return None



if __name__ == "__main__":
    main()