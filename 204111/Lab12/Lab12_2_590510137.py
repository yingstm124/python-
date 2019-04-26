#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 12
#problem 2
#204111 Sec 003

def main():
    # list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
    #               ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
    #               ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
    #               ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
    #               ("9/11/2042", "Event I")]
    # key = "8/05/2019"
    print(search_event(list_x, key))

def search_event(list_x, key):
    ## eliminate zero from key ##
    key_split = key.split("/")
    for num in range (len(key_split)):
        if len(str(int(key_split[num]))) != len(key_split[num]):
            key_split[num] = str(int(key_split[num]))

    key = "/".join(key_split)

    ## add dict ##
    d = dict()
    for i in list_x:
        d[i[1]] = i[0]

    ### check in dict ##
    tuple_ = False
    for element in d:
        if key == d[element]:
            tuple_ = (d[element],element)
            return tuple_

    if tuple_ == False:
        return None


if __name__ == '__main__':
    main()