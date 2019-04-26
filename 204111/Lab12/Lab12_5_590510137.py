#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 12
#problem 5
#204111 Sec 003

def main():
    print('--------')
    #list_x = [19, 48, 175, 290, 873, 7, 43, 69]
    print(radix_int(list_x))

def radix_int(list_x):

    lst = []
    for i in list_x:
        lst.append(i)

    for i in range(len(list_x)):
        min_ = lst[0]
        for j in lst:
            if min_ > j:
                list_x[i] = j
                min_ = j

            list_x[i] = min_

        lst.remove(min_)




if __name__ == '__main__':
    main()
