#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 11
#problem 4
#204111 Sec 003

def main():
    # list_a = [1, 2, [[2, [[145], 34]], [48, 22]]]
    print(sum_nested_list(list_a))


def sum_nested_list(list_a):
    sum_ = 0
    for i in list_a:
        if isinstance(i,list):
            sum_ += sum_nested_list(i)
        else:
            sum_ += i

    return  sum_

if __name__ == '__main__':
    main()



