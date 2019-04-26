def main():
    x = int(input()) ###start
    y = int(input())  ####end
    print(sum_prime_in_range(x, y))

def sum_prime_in_range(x, y):    
    sumprime = 0
    prime = x
### Loop 1 #########################################
    for x in range (x,y+1):
        #### Loop 2 check prime number ####
        for num in range (2,(x//2)+2):
          ##### not prime ######
            if x%num == 0 :
                prime = 0
                break
          ### is prime #######
            prime = x

        if x==2 :
        	prime = x
        
        sumprime += prime
        # if sumprime == 0:
        #     prime = x
        #     sumprime += prime

        # else:
        #     sumprime += prime   

    return sumprime
            


if __name__=="__main__":
    main()



