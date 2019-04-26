#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 5
# 204113 Sec 001

def main():
    list_x = [38, 27, 43, 3, 9, 82, 10]
    merge_sort(list_x, True)
    print('--------')
    print(list_x)

def merge_list(ls_a, ls_b):
    len_a = len(ls_a)
    len_b = len(ls_b)

    i, j = 0, 0
    ls_c = []
    
    # compare
    while i < len_a and j < len_b:
        # a less than b so get front 
        if ls_a[i] < ls_b[j]:
            ls_c.append(ls_a[i])
            i += 1
        else:
            ls_c.append(ls_b[j])
            j += 1
    
    # enough value
    if i < len_a:
        ls_c.extend(ls_a[i:])
    if j < len_b:
        ls_c.extend(ls_b[j:])
    
    return ls_c


def merge_sort(list_x, show_step=False):

    for i in range (len(list_x)):
        list_x[i] = [list_x[i]]
    
    if show_step == True:
        print(list_x)
    
    ls_copy = [i for i in list_x]
    while len(list_x) != 1:
        list_x.clear()
        while len(ls_copy) != 0 :
            if len(ls_copy) == 1:
                list_x.append(ls_copy[0])
                ls_copy.clear()
            else:
                ls_1 = ls_copy.pop(0)
                ls_2 = ls_copy.pop(0)
                list_x.append(merge_list(ls_1, ls_2))
            
        ls_copy = [i for i in list_x]
        
        if show_step == True:
            print(list_x)
    
    if len(list_x) == 1:
        list_x.extend(list_x[0])
        list_x.pop(0)



if __name__ == "__main__":
    main()