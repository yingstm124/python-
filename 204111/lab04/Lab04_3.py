#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 04
# Problem 3
# 204111 Sec 003

def main():
    p1 = int(input(""))
    c1 = int(input(""))
    exp1 = calculate_p2p_evolve_exp(p1,c1)
    print(exp1)

def calculate_p2p_evolve_exp(p,c):
    pidgey_candy = abs(p-1)
    candy = (abs(c)+pidgey_candy)//12
    if p < candy :
        return (p*500)
    else:
        return(candy*500)
if __name__=="__main__":
    main()
