## pascal

def pascal (i,j):

    if i == 0:
        return 1

    elif i == 1:
        return j

    elif i == j:
        return 1


    else:
        return pascal(i-1,j-1)+pascal(i,j-1)

i = int(input("enter row(i) : "))
j = int(input("enter j : "))

print(pascal (i,j))
