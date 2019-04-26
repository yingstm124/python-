def reversedigit(x):
    count = (int(len(str(x)))-1)
    if x<1 :
        return (x%10)*10**count

    else:
        mod = (x%10)*(10**count)
        count -= 1
        return mod + reversedigit(x//10)

x = int(input("enter x : "))
print(reversedigit(x))
