 #        o  ************  o
 #       /|\ *          * /|\
 #       / \ *          * / \
 #   o  ******         ******  o
 #  /|\ *                   * /|\
 #  / \ *                   * / \
 # *******************************

 #!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 07_ex
#problem 1
#204111 Sec 003

def main():
    n = int(input())
    print(pyramid_stairs(n))

def pyramid_stairs(n):

    if n == 0:
         print("")

    else:
        var = n
        count = 1

        while n > 0:
            if n>0:
                ### แถว ###
                for w in range(3):
                    for j in range(n-1):
                        for i in range(6):
                            print(" ",end="")
                        print(" ",end="")

                ####  block 1 ####
                    for a in range(3):
                        if a == 1:
                            if w == 0:
                                print(" o  ",end="*")
                            elif w == 1:
                                print("/|\ ",end="*")
                            elif w == 2:
                                print("/ \ ",end="*")
                            else:
                                print(" ",end="")
                        else:
                            print("",end="")

                    ### base pyramid ###

                    for c in range(5):
                        if w== 0:
                            print("*",end="")
                        else:
                            print(" ",end="")



                    ##### block 2 ####
                    for b in range (count-1):
                        for star in range(10):
                            if w == 0:
                                print(" ",end="")
                            else:
                                print(" ",end="")
                            print("",end="")

                        print("",end="")


                    for f in range(5):
                        if w == 0:
                            print("*",end="")
                        else:
                            print(" ",end="")
                    print("",end="*")

                    for t in range(3):
                        if t == 1:
                            if w == 0:
                                print("  o  ",end="")
                            elif w == 1:
                                print(" /|\ ",end="")
                            elif w == 2:
                                print(" / \ ",end="")
                            else:
                                print(" ",end="")
                        else:
                            print("",end="")

                    print("")

            count += 1
            n -= 1

        ### on the floor  ###3

        for floor in range(((var-1)*10)+22):
            print("*",end="")
        print("")

if __name__ == '__main__':
    main()




