#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 09
#problem 5
#204111 Sec 003

def main():
    num = int(input())
    print(num_to_word(num))

def num_to_word(num):
    if num == 0:
        return "zero"

    list_3 = [""," thousand "," million "," billion "]

### divide ####
    list_n = []
    i = 0
    word = ""
    while num>0:
        n = num%1000
        list_n.insert(0,n)
        num//=1000

    for i in range (len(list_n)):
        n = list_n[i]
        word += ""
        word += three_digits_to_word(n)
        word += ""
        if int(list_n[i]) != 0:
            word += list_3[len(list_n)-1-i]

    word = word.strip()

    return word



def three_digits_to_word(n):

    list_1 = ["", "one", "two", "three", "four", "five",\
              "six", "seven", "eight", "nine", "ten",\
              "eleven", "twelve", "thirteen", "fourteen","fifteen",\
              "sixteen", "seventeen", "eighteen","nineteen"]
    list_2 = ["",""," twenty"," thirty"," forty"," fifty"," sixty"," seventy"," eighty"," ninety"]



    if n <= 19:
        word = " "+list_1[n]



    elif n <= 99:
        a,b = divmod(n,10)
        if b == 0:
            word = " "+list_2[a]
        else:
            word = " "+list_2[a]+"-"+list_1[b]



    elif n >= 100 :
        a,modu = divmod(n,100)
        b,c = divmod(modu,10)

        if b*10 + c <= 19:
            word =  " "+list_1[a]+" hundred"+" "+list_1[b*10 + c]
        elif c == 0 :
            word = " "+list_1[a]+" hundred"+list_2[b]
        else:
            word =  " "+list_1[a]+" hundred"+list_2[b] + "-" + list_1[c]

    word = word.strip()

    return word


if __name__ == '__main__':
    main()
