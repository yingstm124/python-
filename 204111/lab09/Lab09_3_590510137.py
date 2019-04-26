#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 09
#problem 3
#204111 Sec 003
def main():
    list_a = [1,2,3,4]
    n = int(input())
    print(nondest_rotate_list(list_a,n))


def nondest_rotate_list(list_a,n):

    ## positive let right ###
    if n >= 0:
        for i in range (n):
            keep = list_a[len(list_a)-1]
            del list_a[len(list_a)-1]
            list_a.insert(0,keep)

    ## negative let left ###
    elif n<0:

        for i in range (abs(n)):
            keep = list_a[0]
            del list_a[0]
            list_a.append(keep)
    return list_a


if __name__ == '__main__':
    main()
