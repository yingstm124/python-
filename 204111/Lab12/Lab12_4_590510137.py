#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 12
#problem 4
#204111 Sec 003

def main():
    p1 = [ (0, 5), (2, 6),(4,6)]
    p2 = [(2, -6),(4,11)]
    print(polynomial_addition(p1, p2))

def polynomial_addition(p1, p2):
    sort_p1 = (sorted(p1, reverse=True))
    sort_p2 = (sorted(p2, reverse=True))


    len_sort_p1 = len(sort_p1)
    len_sort_p2 = len(sort_p2)

    i_p1 = 0
    i_p2 = 0

    lst = []


    while (i_p1 < len_sort_p1) and (i_p2 < len_sort_p2):

        if sort_p1[i_p1][0] == sort_p2[i_p2][0]:
            sum_ = sort_p1[i_p1][1] + sort_p2[i_p2][1]
            if sum_ != 0:
                tuple_ = (sort_p1[i_p1][0], sum_)
                lst.append(tuple_)
            i_p1 += 1
            i_p2 += 1

        elif sort_p1[i_p1][0] > sort_p2[i_p2][0]:
            if sort_p1[i_p1][1] != 0 :
                lst.append(sort_p1[i_p1])
                i_p1 += 1

        elif sort_p1[i_p1][0] < sort_p2[i_p2][0]:
            if sort_p2[i_p2][1] != 0:
                lst.append(sort_p2[i_p2])
                i_p2 += 1

    if len_sort_p1 > i_p1:
        lst.extend(sort_p1[i_p1:])
    if len_sort_p2 > i_p2:
        lst.extend(sort_p2[i_p2:])

    return  lst


if __name__ == '__main__':
    main()

