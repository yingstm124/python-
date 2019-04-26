def main():
    list_x = \
    [19, 48, 175, 290, 873, 7, 43, 69]
    radix_int(list_x, True)
    print('--------')
    print(list_x)

    # test
    # assert(radix_int([19, 48, 175, 290, 873, 7, 43, 69], True)==[7, 19, 43, 48, 69, 175, 290, 873])
    # assert(radix_int([0, 1, 10, 10, 100], True)==[0, 1, 10, 10, 100])
    # assert(radix_int([19, 8, 5, 29, 873, 7000, 13, 769], True)==[5, 8, 13, 19, 29, 769, 873, 7000])
    # print("pass")


def radix_int(list_x, show_step=False):
    
    list_x_copy = [str(i) for i in list_x]

    # find max lenght
    max_lenght = 0 
    for i in range (len(list_x_copy)):
        if len(str(list_x_copy[i])) > max_lenght:
            max_lenght = len(str(list_x_copy[i]))

    # fill zero before
    for j in range (len(list_x_copy)):
        fill_zero = max_lenght - len(str(list_x_copy[j]))
        for i in range (fill_zero):
            list_x_copy[j] = "0" + str(list_x_copy[j])

    # loop
    index = max_lenght-1
    while index >= 0:
        # insertion sort
        for j in range (1,len(list_x_copy)):
            i = j
            while not (i <= 0):
                if int(list_x_copy[i-1][index]) > int(list_x_copy[i][index]):
                    list_x_copy[i-1], list_x_copy[i] = list_x_copy[i], list_x_copy[i-1]
                    list_x[i-1], list_x[i] = list_x[i], list_x[i-1]
                i -= 1            
             
        index -= 1 
        if show_step == True:
            print(list_x)


if __name__ == "__main__":
    main()