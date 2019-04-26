
def main():
    num = int(input())
    print(reverse_num(num))


def reverse_num(num):
    count = (int(len(str(num)))-1)
    if num<1 :
        return (num%10)*10**count

    else:
        mod = (num%10)*(10**count)
        count -= 1
        return mod + reverse_num(num//10)

if __name__ == '__main__':
    main()
