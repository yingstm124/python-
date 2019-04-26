def main():
    n = int(input())
    print(longest_digit_run(n)) 

def longest_digit_run(n):
    #num = 1
    count = 1
    check = 0
    i = 1
    x = n
    
    
    while n>0:
        x = (n%(10**(i+1)))//(10**i)
        y = (n%(10**i)//10**(i-1))

        if x==y :
            count +=1
            
        elif x!= y:
            count = 1

        ####  check #####

        if count > check :
            check = count

        n = n//10

    return check

if __name__=="__main__":
	main()
