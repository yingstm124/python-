#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 3
# 204113 Sec 001

def main(): 
    # test prime
    assert(prime_factorize(222)==[2,3,37,1])
    assert(prime_factorize(0)==[0])
    assert(prime_factorize(13)==[13,1])
    assert(prime_factorize(39)==[3,13,1])
    assert(prime_factorize(390)==[2,3,5,13,1])
    assert(prime_factorize(190)==[2,5,19,1])
    assert(prime_factorize(290)==[2,5,29,1])
    assert(prime_factorize(1800)==[2,2,2,3,3,5,5,1])
    print("prime_factor is pass")

    # test lcm
    assert(lcm([390,10,39,80])==3120)
    assert(lcm([40,25,5])==200)
    assert(lcm([0,0,0,0])==0)
    assert(lcm([1,1,1,1])==1)
    assert(lcm([66,77,88,99,111])==205128)
    assert(lcm([13,17,8])==1768)
    assert(lcm([65, 6, 10])==390)
    assert(lcm([490,9,2])==4410)
    assert(lcm([100,10000,10000])==10000)
    assert(lcm([500,50,77])==38500)
    assert(lcm([57,59,21])==23541)
    assert(lcm([255,133,12])==135660)
    assert(lcm([0])==0)

    print("lcm is Pass")


# recursive
# sort min to max
# return int x
def prime_factorize(x, i=2):

    if x == 0:
        return [0]

    # base case when divider less than number
    elif i > (x):
        return [1]

    # factor that can divid and return prime
    elif x%i == 0:
        return [i] + prime_factorize(x/i ,i=2)   
        
    i += 1
    return prime_factorize(x, i)

def lcmfactor(x, y):
    # factor of x,y

    x_ls = prime_factorize(x)
    y_ls = prime_factorize(y)

    # copy x_ls for remove double value 
    x_ls_copy = [i for i in x_ls]

    ls = []
    for i in range (len(x_ls)):
        count = 0

        # loop for find double value both of x_ls and y_ls
        for y in y_ls:
            # x_ls value as y_ls value
            if x_ls[i] == y:
                # delete y_ls and x_ls copied
                y_ls.remove(y)
                x_ls_copy.remove(y)
                count += 2
                # out of loop 
                break
        
        # if double value 
        if count >= 2:
            amount = count//2
            # get append value
            for k in range (amount):
                ls.append(x_ls[i])
    
    # empty case 
    if ls == []:
        ls = [0]
        return ls
    
    # connect to another value of x_ls and y_ls and ls that is double value  
    ls = ls + y_ls + x_ls_copy
    # sort min to max
    ls.sort()

    return ls

def lcm(alist):
    # alist is one length
    if len(alist)==1:
        return alist[0]
    # loop find Lcm factor
    first_ = alist[0]
    for i in range (1,len(alist)):        
        ls_first = lcmfactor(first_,alist[i])
        multi = 1
        for k in range (len(ls_first)):
            multi *= ls_first[k]
        first_ = multi

        #print("ls_first {0}".format(ls_first))

    # mulit value
    multi = 1
    for k in range (len(ls_first)):
            multi *= ls_first[k]
    
    return multi

if __name__ == "__main__":
    main()




