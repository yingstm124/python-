#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 09
#problem 4
#204111 Sec 003

def main():
    list_a = [1,2,3,4]
    n = int(input())
    dest_rotate_list(list_a, n)


def dest_rotate_list(list_a, n):
    list_b = []
## positive n
    if n > len(list_a):
        n = n%4
    elif n>0:
        n = n
## negative n
    else:
        n = abs(n)
        n = n%4
        n = -(n)

### let right positive ##
    if n>0:
        for i in range (n):
            keep = list_a[len(list_a)-1]
            del list_a[len(list_a)-1]
            list_b.insert(0,keep)

        list_b = list_b + list_a

### let left negative ###
    elif n<0:
        n = abs(n)
        for i in range (n):
            keep = list_a[0]
            del list_a[0]
            list_b.append(keep)

        list_b = list_a + list_b

    print(list_b)


if __name__ == '__main__':
    main()
