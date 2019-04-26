def enter_data ():
    lst_data = []
    print("----plase enter a data and 0 when you want to stop----- ")
    while True:
        try:
            data = input("Enter the data :")
            if data == "0" :
                break
            elif data >= "0" and data <= "9":
                try:
                    data = int(data)
                    lst_data.append(data)
                except ValueError:
                    print("ValueError")
            else:
                print("error")
        except KeyboardInterrupt:
            print("pass")
            break

    mean_ = findmean(lst_data)
    print("mean is {0}".format(mean_))


def findmean(lst_data):
    sum_ = 0
    total_number = 0
    for i in range (len(lst_data)):
        total_number += 1
        sum_ += lst_data[i]

    mean_ = sum_/total_number
    return mean_


enter_data()

