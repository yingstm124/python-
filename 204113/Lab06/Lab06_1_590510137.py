#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 06
# Problem 1
# 204113 Sec 001


def main():

    show_step = True
    result = eratosthenes(10, show_step)
    print("----")
    print(result)

    # test 
    # assert(eratosthenes(67)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67])
    # assert(eratosthenes(54)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,])
    # assert(eratosthenes(110)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109])
    # assert(eratosthenes(37)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    # assert(eratosthenes(2)==[2])
    # assert(eratosthenes(1)==[])
    # assert(eratosthenes(0)==[])
    # assert(eratosthenes(100)==[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
    # assert(eratosthenes(20)==[2, 3, 5, 7, 11, 13, 17, 19])

def eratosthenes(n, show_step=False):
    ls_n = [i for i in range(2,n+1)]
    result_ls = []
    i = 2
    while i*i <= n or n == 2:
        # prime number
        if i%2 != 0 or i == 2:
            if show_step == True:
                print(i,end=": ")

            result_ls.append(i)
            # sieve
            for num in ls_n:
                if num%i == 0 :
                    ls_n.remove(num)

            if show_step == True:
                print(ls_n)
        
        if n != 2:    
            i = ls_n[0]
        else:
            n -= 1

    result = result_ls + ls_n

    return result
    

if __name__ == "__main__":
    main()