#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 1
# 204113 Sec 001

def main():
    # test linearserch
    assert(linear_search(5, [1,2,3,4])==None)
    assert(linear_search(3,[1,2,3,4,5])==2)
    assert(linear_search("D",["A","B","C","D","E"])==3)
    assert(linear_search(3.1,[1.0,2.1,3.0,3.1,4])==3)
    assert(linear_search(6,[1,2,3,3,4,6])==5)
    assert(linear_search("Vat", ["V","F","Vat"])==2)
    assert(linear_search(0.3333, [1.2,1.333,0.3332])==None)
    assert(linear_search("R",["A","B","M"])==None)
    assert(linear_search("WOOOO", ["Wooo"])==None)
    assert(linear_search(0.3333,[0.3333])==0)

    print("linearserch is pass")

def linear_search(key, l):
    # finding keyword
    index = 0
    found = False
    for i in range (len(l)):
        # found !
        if l[i] == key:
            found = True
            break
        else:
            index += 1
            found = False
    # return index when found it
    if found:
        return index
    else:
        return None

if __name__ == "__main__":
    main()
