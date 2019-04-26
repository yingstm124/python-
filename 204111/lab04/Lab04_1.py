#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 1
# 204111 Sec 003

def main():
    first1 = int(input(""))
    second1 = int(input(""))
    result1 = love6(first1,second1)
    print(result1)

def love6(first,second):
    if first ==6 or second ==6:
        return True
    elif (first+second == 6):
        return True
    elif (first-second==6 or second-first==6):
        return True
    else:
        return False

if __name__=="__main__":
    main()

    
        
        
