def main():
    list_x = [10,"hello",23.5,4]
    print(classify(list_x))

def classify(list_x):
    list_a = []
    list_b = []
    list_c = [] ##str

    for i in range(len(list_x)):
        a = list_x[i]
        if isinstance(a,int):
            list_a.append(a)
        elif isinstance(a,float):
            list_b.append(a)
        else:
            list_c.append(a)

    i+=1

    return list_a,list_b,list_c

if __name__ == '__main__':
    main()











