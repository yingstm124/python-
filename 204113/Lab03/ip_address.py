def main():
    mode = 1
    text = "10.28.4.2"
    print(IP_encode(mode,text))

def decimal_to_binary_unsign(str_):
    num = int(str_)
    sum_ = 0
    i = 0
    while num > 0:
        reminder = num%2
        sum_ += reminder*(10**i)

        num //= 2
        i += 1

    return str(sum_)

def unsign_binary_to_decimal(bits32_str):

    result = 0
    print(bits32_str)
    for i in range (len(bits32_str)-1,-1,-1):
        if bits32_str[i] == "1":
            result += 2**(len(bits32_str)-i-1)
        
    
    print(result)
    return

def IP_encode(mode,text):
    ## split text ##
    text_ls = text.split(".")
    print(text_ls)

    ## mode 1 IP address to unsignbits ##
    new_binary_ls = []
    for decimal in text_ls:
        binary_str = decimal_to_binary_unsign(decimal)
        binary_str = binary_str.zfill(8)
        new_binary_ls.append(binary_str)

    bit_32 = "".join(new_binary_ls)

    print(new_binary_ls)
    print(bit_32)
    ## decimal##
    

    ## mode 2 decimal to binary to IP address ##

    return

if __name__ == "__main__":
    main()


