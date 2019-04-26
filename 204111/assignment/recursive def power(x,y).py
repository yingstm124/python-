## power assignment 5 no.5

def power(x, y):
    if y == 1:
        return x
    else:
        y -= 1
        return x*power(x,y)

x = int(input("enter x : "))
y = int(input("enter y : "))

print(power(x,y))
