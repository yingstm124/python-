#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 4
# 204111 Sec 003
def main():
    l1 = int(input(""))
    t1 = int(input(""))
    w1 = int(input(""))
    
    h1 = int(input(""))
    l2 = int(input(""))
    t2 = int(input(""))
    w2 = int(input(""))
    h2 = int(input(""))
    print(is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2))


def is_overlapped(l1,t1,w1,h1,l2,t2,w2,h2):
#non-overlap#
    #t2>(t1+h1)__2movedown#
    #t1>(t2+h2)__2moveup#
    #(l1+w1)>l1__2left#
    #l1>(l2+w2)__2right#
    
    if (t1+h1)<t2 or (t2+h2)<t1 or (l1+w1)<l2 or (l2+w2)<l1:
        return False
    else:
        return True

if __name__=="__main__":
    main()
    

