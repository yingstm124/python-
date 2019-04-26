#!/usr/bin/eny python3
#sutimar pengpinij
#590510137
#Lab 10
#problem 4
#204111 Sec 003

def main():
    line = str(input())
    print(uniform(line))


def uniform(line):
    lst_line =  list(line)

    lst_newline = []
    amount_lower = 0
    amount_upper = 0

    ### count amount of  low & up and append a lst ###

    for i in range (len(line)):
        if lst_line[i] >= "a" and lst_line[i] <= "z":
            lst_newline.append(lst_line[i])
            amount_lower += 1

        if lst_line[i] >= "A" and lst_line[i] <= "Z":
            lst_newline.append(lst_line[i])
            amount_upper += 1

    ### check which is more ? ###
    if  amount_upper == amount_lower:

        if lst_newline[0] >= "a" and lst_newline[0] <= "z":
            line = line.lower()
        elif lst_newline[0] >= "A" and lst_newline[0] <= "Z":
            line = line.upper()

    elif amount_lower > amount_upper:
        line = line.lower()

    else:
        line = line.upper()

    return line

if __name__ == '__main__':
    main()
