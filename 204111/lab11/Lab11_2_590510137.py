#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 11
#problem 2
#204111 Sec 003

import copy

def main():
    list_a = input()
    row = input()
    col = input()
    print(remove_row_col(list_a, row, col))


def remove_row_col(list_a, row, col):
    list_b = copy.deepcopy(list_a)
    rows = len(list_b[:])
    for r in range(rows):
        count = 0
        for c in range(len(list_b[r])):
            count += 1
    colums = count

    if (col < 0 and abs(col) <= colums) or (col >= 0 and col < colums):
        ### cut a colums ##
        for i in list_b:
            i.pop(col)

    if (row < 0 and abs(row) <= rows) or (row >= 0 and row < rows):
        ## cut a rows ##
        list_b.pop(row)

    return list_b

if __name__ == '__main__':
    main()

