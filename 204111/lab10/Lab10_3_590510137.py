#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 10
#problem 3
#204111 Sec 003
def main():
    message = str(input())
    pattern = str(input())

    patterned_message(message,pattern)

def patterned_message(message,pattern):
    ### eliminate specs ###
    lst_mess = []
    for i in range (len(message)):
        if message[i] != " ":
            lst_mess.append(message[i])

    ## convert str of pattern to the list ##
    lst_pat = list(pattern)
    lst_pat.sort(key=len)

    ## instead index of message on * ##
    i = 0
    for j in range(len(lst_pat)):
        if i >= len(lst_mess):
            i = 0

        if lst_pat[j] == "*":
            lst_pat[j] = lst_mess[i]
            i += 1

    ## convert to str from list ##
    pattern_mess = "".join(lst_pat)

    print (pattern_mess)


if __name__ == '__main__':
    main()

