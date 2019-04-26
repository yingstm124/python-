def main():
    x = int(input())
    y = int(input())
    print(gcd(x, y))

def gcd(x, y):
    mod = x%y
    if mod == 0:
        return y
    else:
        x = y
        y = mod
        return gcd(x,y)

if __name__=="__main__":
    main()


