#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 08
# Problem 1
# 204113 Sec 001

def main():
    ex1 = {'a': 35, 'b': 26, 'c': 12,'d': 16, 'e': 17, 'f': 20}
    print(huffman(ex1))  

def huffman(freq):

    # base case dict have only two args
    # zip [0,1]
    if len(freq) == 2:
        return dict(zip(freq.keys(), ["0","1"])) 

    # key_1 is lowest key
    # key_2 is low key

    key_1, key_2 = find_low(freq)
    val_1, val_2 = freq.pop(key_1), freq.pop(key_2)
    
    # print(key_1, key_2)
    # print(val_1, val_2)

    # add dict sum val
    freq[key_1 + key_2] = val_1 + val_2

    #print(freq)

    root = huffman(freq)
    pop_root = root.pop(key_1 + key_2)

    # seperate
    root[key_1], root[key_2] = pop_root + "0", pop_root + "1"
    
    
    return root

def find_low(freq):
    # kv[1] is value
    sort_d = sorted(freq.items(), key=lambda kv : kv[1])


    # frequecy equal
    if sort_d[0][1] == sort_d[1][1]:
        # loop find frequecy equal
        dict_same = find_frequecy(sort_d, sort_d[0][1])
        sort_d = sorted(dict_same.items(), key=lambda kv: kv[0])
    
    return sort_d[0][0], sort_d[1][0]

def find_frequecy(sorted_ls, value_same):

    dict_same = dict()
    for tup in sorted_ls:
        if tup[1] == value_same:
            dict_same[tup[0]] = tup[1]

    return dict_same



if __name__ == "__main__":
    main()
