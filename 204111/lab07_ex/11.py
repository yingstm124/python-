n = 1


for i in range(n):
    for j in range (14):
        if j == 0 :
            print("    o",end="  ")
        elif j == 13:
            print("  o")
        else:
            print("*",end="")


    for k in range (14):
        if k == 0:
            print("   /|\ ",end="*")
        elif k == 11:
            print("* /|\ ")
        else:
            print(" ",end="")

    for w in range (14):
        if w == 0:
            print(" / \ ",end="*")
        elif w == 11:
            print("* / \ ")
        else:
            print(" ",end="")



for z in range ((n*10)+12):
    print("*",end="")

