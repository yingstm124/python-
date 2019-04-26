#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 10
#problem 1
#204111 Sec 003


def main():
    n = int(input())
    sep = input()

    if sep == '' :
        square_frame(n)
    else:
        sep = str(sep)
        square_frame(n,sep)

def square_frame(n, sep=' '):
    ### create a list ###
    lst = []
    for num in range(1,4*(n-1)+1):
        lst.append(str("{:02d}".format(num)))

    ## total of a list ###
    numlst = int(len(lst))

    ### square frame ###
    for j in range(n):
        ## frist vertical ###
        if j == 0:
            print(sep.join(lst[:n]))
        else:
        ## except only second vertical don't take down a new line ###
            if j>1:
                print("")

            for a in range(n):
                ## check a final line ###
                if j==n-1:
                    print(sep.join(lst[numlst-(n-1):numlst-(n-1)-n:-1]))
                    break
                ## 1st rows ##
                elif a == 0:
                    print(lst[numlst-j],end=((2*(n-2))+(n-1))*sep)
                ## last rows ###
                elif a == n-1:
                    print(lst[(n-1)+j],end="")



if __name__ == '__main__':
    main()

