#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 2
# 204111 Sec 003

def main():
    x = float(input(""))
    print("%.6f"%float_to_bin(x))


def float_to_bin(x):
    y = x
    x = abs(x)
    frontbin = x//1
    backbin = (x - x//1)
    #print("frontbin ",frontbin)
    #print("backbin ",backbin)


    debi_f = 0
    i = 0
####frontbin####
    while frontbin > 0:
        debi_f = debi_f + ((frontbin%2)//1)*(10**i)
        frontbin = frontbin//2
        i +=1
    #print("debi_f ",debi_f)
    
#####backbin#####
    check = backbin/2
    debi_b = 0
    i = 0
    while i <= 6 :
        check = (check*2)
        if check >= 1:
            check = check-1
            debi_b = 1*10**(-i)+debi_b
        else:
            debi_b = (check//1)*10**(-i) + debi_b
        i +=1
        
    #print("debi_b ",debi_b)
    
            
###including###
    debi = debi_f + debi_b

###trap in x###
    if y<0:
        debi = -1*(debi)
    else:
        debi = debi

    return (debi) 

if __name__=="__main__":
    main()

