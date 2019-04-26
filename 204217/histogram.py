
run = True
ls_count = [0 for i in range (10)]
while run:
    n = int(input("Enter the number (key -1 for finish): "))
    if n == -1:
        run = False
    elif n < 10: 
        if n == 0:
            ls_count[0] += 1
        elif n == 1:
            ls_count[1] += 1
        elif n == 2:
            ls_count[2] += 1
        elif n == 3:
            ls_count[3] += 1
        elif n == 4:
            ls_count[4] += 1
        elif n == 5:
            ls_count[5] += 1
        elif n == 6:
            ls_count[6] += 1
        elif n == 7:
            ls_count[7] += 1
        elif n == 8:
            ls_count[8] += 1
        elif n == 9:
            ls_count[9] += 1

for i in range (10):
    print(i,end=" ")

    for j in range (ls_count[i]):
        print("*",end="")
    
    print("")
    
    
    



