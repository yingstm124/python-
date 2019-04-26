def main():
    # list_x = [[2, 3, 4],
    #           [1, 2, 3],
    #           [5, 8,5,6,7,8,9],
    #           [2 ]]
    print(square_matrix(list_x))


def square_matrix(list_x):
    lenrow = len(list_x)
    lencol_max = len(list_x[0])

    for lst_x in list_x:
        lencol = len(lst_x)
        if lencol > lencol_max:
            lencol_max = lencol

    lencol = lencol_max
    if lenrow > lencol:
        lenmax = lenrow
    else:
        lenmax = lencol

    ## add col ##
    for lst_col in list_x:
        if len(lst_col) != lenmax:
            for g in range(abs(len(lst_col) - lenmax)):
                lst_col.append(0)

    ## add row ##
    for j in range(abs(lenmax - lenrow)):
        lst_row = []
        for row in range(lenmax):
            lst_row.append(0)

        list_x.append(lst_row)



if __name__ == '__main__':
    main()