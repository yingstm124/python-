def main():
    list_x = [("11/1/1900", "Event A"), ("5/12/2001", "Event B"),
    ("5/12/2002", "Event C"), ("21/8/2008", "Event D"),
    ("9/3/2013", "Event E"), ("11/3/2017", "Event F"),
    ("7/5/2019", "Event G"), ("29/2/2032", "Event H"),
    ("9/11/2042", "Event I")]
    event = search_event(list_x, "21/08/2008", True)
    print("---")
    print(event)
  
def search_event(list_x, key, show_step=False):

    # reverse and fill zero into key
    key_ls = key.split("/")
    for i in range (len(key_ls)-1):
        if i == 0 or i == 1:
            lenght = 2-len(key_ls[i])
            for fill_zero in range (lenght):
                key_ls[i] = "0" + key_ls[i]
    key_ls.reverse()
    key = "".join(key_ls)



    date_ls = [ list_x[i][0] for i in range (len(list_x)) ]
    # reverse and fill zero into date
    for i in range (len(date_ls)):
        date_ls[i] = date_ls[i].split("/") 
        for j in range (len(date_ls[i])-1):
            # date or month
            if j == 0 or j == 1:
                length = 2-len(date_ls[i][j])
                for fill_zero in range (length):
                    date_ls[i][j] = "0" + date_ls[i][j]
        date_ls[i].reverse()
        date_ls[i] = "".join(date_ls[i])

    list_x_copy = []
    for i in range (len(list_x)):
        list_x_copy.append((date_ls[i], list_x[i][1]))

    
    # compare date and binary search
    lo = 0
    hi = len(list_x)-1
    found = False

    while not found and lo <= hi:
        
        mid = (lo + hi)//2
        # keep left
        if int(key) < int(list_x_copy[mid][0]):
            hi = mid - 1
        # keep right
        elif int(key) > int(list_x_copy[mid][0]):
            lo = mid + 1
        # found!
        else:
            found = True
        
        if show_step == True:
            print("[{0}]".format(mid),end=": ")
            print(list_x[mid][0])

    if found == True:
        return list_x[mid]
    else:
        return None





if __name__ == "__main__":
    main()