
def binarysearch_recursive (list_, key, found=False):
    
    mid = len(list_)//2
    # base case
    if key == list_[mid]:
        found = True
        return ("found") 

    elif len(list_) <= 1:
        found = False
        return ("not found")

    if key < list_[mid]:
        return binarysearch_recursive(list_[:mid], key, found)
    
    elif key > list_[mid]:
        return binarysearch_recursive(list_[mid:], key, found)


def main():
    test_ls = [1,2,3,4,5,7,8,9,1]
    key = 1
    print(binarysearch_recursive (test_ls, key))

if __name__ == "__main__":
    main()


