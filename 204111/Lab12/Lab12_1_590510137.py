#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 12
#problem 1
#204111 Sec 003

def main():
    print("---")
    #list_x = ["02/10/100", "4/12/1", "19/7/20", "11/9/2001"]
    sort_date(list_x)

def sort_date(list_x):

    list_x_copy = [ i for i in list_x]

    ## split ##
    lst_split = []
    for i in range (len(list_x_copy)):
        split  = list_x_copy[i].split("/")
        lst_split.append(split)

    ## add zero ##
    for i in range (len(lst_split)):
        for j in range (len(lst_split[i])):
            ## except only year ## not add zero ##
            if (j != 2) and (len(lst_split[i][j]) == 1):
                lst_split[i][j] = "0"+lst_split[i][j]

        lst_split[i].reverse()
        lst_split[i] = "/".join(lst_split[i])

    lst_split.sort()

    ## reverse back ##
    lst_back = []
    for i in range (len(lst_split)):
        lst_split_back = lst_split[i].split("/")
        lst_split_back.reverse()
        split_back = "/".join(lst_split_back)
        lst_back.append(split_back)

    ## eliminate zero ##
    for i in range (len(lst_back)):
        lst_back[i] = lst_back[i].split("/")
        for j in range (len(lst_back[i])):
            if len(str(int(lst_back[i][j]))) != len(lst_back[i][j]):
                lst_back[i][j] = str(int(lst_back[i][j]))

        lst_back[i] = "/".join(lst_back[i])


    ## put in list_x ##
    for k in range (len(list_x)):
        list_x[k] = lst_back[k]




if __name__ == '__main__':
    main()