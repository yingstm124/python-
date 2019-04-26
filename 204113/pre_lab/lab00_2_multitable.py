def main():
    multiplication_table(10)

def multiplication_table(n):
    for i in range (n+1):
        if i == 0 :
            print("*",end="\t")
            for k in range (1,n+1):
                print(k,end="\t")
            print("")
                
        else:
            if i == 1 :
                print(i,end="\t")
            else :
                print(i,end="")
                for blank in range (i):
                    print("",end="\t")
            for k in range (i,n+1):
                print(i*k,end="\t")
            print("")
        
            
if __name__ == "__main__":
    main()
