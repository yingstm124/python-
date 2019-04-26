n = 2

for a in range (n):

    ## space ##

    for w in range (n):
        for j in range(w*4):
            for i in range (w*8):
                print("_",end="")
            print("")
    print("",end="")

    ## head ###
    for b in range (17):
        if b == 0 or b == 15:
            print(" ",end="")
        elif b == 1 or b == 16:
            print("o",end=" ")
        elif b == 8 :
            for c in range ((a)*10):
                print(" ",end="")
        else:
            print("*",end="")
    print("")

    ## body ##
    for c in range(17):
        if c == 0 or c == 14:
            print("/",end="")
        elif c == 1 or c == 15:
            print("|",end="")
        elif c == 2 or c == 16:
            print("\ ",end="")
        elif c == a*(17/2):
            for c in range ((a)*10):
                print(" ",end="")
        else:
            print(" ",end="")
    print("")

    ## leg ###
    for e in range (17):
        if e == 0 or e == 14:
            print("/",end="")
        elif e == 2 or e == 16:
            print("\ ",end="")
        else:
            print(" ",end="")




    print("")






