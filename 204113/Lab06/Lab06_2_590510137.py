#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 2
# 204113 Sec 001

def main():
    list_x = ["12/10/4", "11/10/2000"]
    sort_date(list_x, True)
    print("---")
    print(list_x)

    # assert(sort_date(["11/1/1999", "5/12/1999", "19/2/1999", "11/9/1999"], True) == ['11/1/1999', '19/2/1999', '11/9/1999', '5/12/1999'])
    # assert(sort_date(["12/10/2000", "11/10/2000"], True) == ["11/10/2000", "12/10/2000"])
    # print("pass")

def sort_date(list_x, show_step=False):
    list_x_copy = [i for i in list_x]
    # reverse list and fill zero before sorting 
    for i in range (len(list_x_copy)):
        list_x_copy[i] = list_x_copy[i].split("/")
        # fill zero & reverse list
        for j in range (len(list_x_copy)-1):
            # date
            if j == 0:
                length = 2 - len(list_x_copy[i][j])  
                for k in range(length):
                    list_x_copy[i][j] = "0" + list_x_copy[i][j]
            # month
            elif j == 1:
                length = 2 - len(list_x_copy[i][j])
                for k in range(length):
                    list_x_copy[i][j] = "0" + list_x_copy[i][j]
        

        list_x_copy[i].reverse()
        list_x_copy[i] = "".join(list_x_copy[i])

    # sorting 
    for j in range (1,len(list_x_copy)):
        i = j
        while not (i <= 0):
            if int(list_x_copy[i-1]) > int(list_x_copy[i]):
                list_x_copy[i-1], list_x_copy[i] = list_x_copy[i], list_x_copy[i-1]
                list_x[i-1], list_x[i] = list_x[i], list_x[i-1]

            i -= 1

        if show_step == True:
            print(j,end=": ")
            print(list_x)




if __name__ == "__main__":
    main()

