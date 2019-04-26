#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 11
#problem 3
#204111 Sec 003

def main():
    board = [[2, 7, 6],
             [9,5, 1],
             [3, 4, 8]]

    print(is_magic_square(board))

def is_magic_square(board):
    rows = len(board[:])
    colums = rows

    ## create lst n**2 ##
    lst = []
    for i in range (1,(rows**2)+1):
        lst.append(i)

    ## check 1-n**2 ##
    count = 0
    for r in range (rows):
        for i in board[r]:
            if i in lst:
                count += 1
                lst.remove(i)

    ## check sum all of vertical horizontal diagonal ###
    if count == (rows**2):
        ## horizontal ##
        lst_h = [sum(board[r]) for r in range(rows)]

        ## vertical  ##
        lst_v = []
        for j in range(rows):
            sum_ = 0
            for i in board:
                sum_ += i[j]
            lst_v.append(sum_)

        ## diagonal ##
        lst_d = []
        sum_ = 0
        for r in range(rows):
            sum_ += board[r][r]
        lst_d.append(sum_)

        sum_ = 0
        for r in range(rows - 1, -1, -1):
            sum_ += board[r - 1][-r]
        lst_d.append(sum_)

        ## check point ##
        lst_v = check(lst_v)
        lst_h = check(lst_h)
        lst_d = check(lst_d)

        if lst_v == False or lst_h == False or lst_d == False:
            return False
        else:
            return True

    else:
        return  False


def check(lst):
    check = lst[0]
    for i in lst :
        if  check != i:
            lst = False
    return  lst


if __name__ == '__main__':
    main()