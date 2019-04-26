#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 09
#problem 1
#204111 Sec 003

def main():
    str1 = str(input())
    str2 = str(input())
    print(is_anagram(str1,str2))


def is_anagram(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = sorted(str1)
    str2 = sorted(str2)

    str_1 =[]
    str_2 =[]

###  add str_1  ###
    for i in range (len(str1)):
        if str1[i] <= "z" and str1[i] >= "a":
            str_1.append(str1[i])


## add str_2 ###
    for i in range (len(str2)):
        if str2[i] <= "z" and str2[i] >= "a" :
            str_2.append(str2[i])

### checking point ####
    if str_1 == str_2:
        return True
    else:
        return False

if __name__ == '__main__':
    main()

