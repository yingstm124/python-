def main():
    # n = int(input())
    # for i in range (n):
    #     mode = int(input())
    #     text = str(input())
    mode = 1
    text = "10.28.4.2"
    print(IP_encode(mode,text))

def IP_encode(mode,text):
    
    ## mode 1 ip address to decimal ##
    if mode == 1:
        ## split text ##
        text_ls = text.split(".")
        ip_address = int(int(text_ls[0])<<24)+int(int(text_ls[1])<<16)+int(int(text_ls[2])<<8)+int(int(text_ls[3]))
        ans = ip_address
    ## mode 2 decimal to ip address ##
    else:
        ls_ = []
        for i in range (4):
            dec = (int(text) >> (i<<3) & 255)
            ls_.insert(0,dec)
        str_ls = list(map(str,ls_))
        ans = ".".join(str_ls)
              
    return ans

if __name__ == "__main__":
    main()
