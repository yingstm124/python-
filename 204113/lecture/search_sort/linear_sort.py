def main():
    list_ = [4,5,2,3,1]
    print(linear_sort(list_))
    #print(merge_sort(list_))

def linear_sort (list_):
    # sort to min to max
    for i in range(len(list_)):
        j = i
        while j > 0 and list_[j-1] > list_[j] :
            list_[j-1],list_[j] = list_[j],list_[j-1]
            j -= 1

    return list_ 

#def merge_sort(list_):




if __name__ == "__main__":
    main()