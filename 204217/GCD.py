def main():
    running = True
    data_ls = [] 
    while running:
        a = int(input("Enter a number : "))
        b = int(input("Enter a number : "))
        gcd = GCD(a,b)
        print("GCD = %d"%gcd)
        data_ls.append(gcd)
        ask = input("Continue? : ")
        print("")
        check = continue_ask(ask)
        
        if check == False:
            running = False
            break
        
            
    print(data_ls)

    
def continue_ask(str_ask):
    if str_ask == "y":
        return True
    elif str_ask == "n":
        return False

def GCD(a,b):
    try:
        while b != 0:
            reminder = a % b
            a = b
            b = reminder
        
        return a

    except ZeroDivisionError:
        print("None")

if __name__ == "__main__":
    main()