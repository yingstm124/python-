
def main():
    word = 'get'
    print(permute(word))

def permute(word):
    
    ls = []
    for i in range (len(word)):
        if i == 0:
            ls.append(word[i])

        elif i > 0:
            ls_ = []
            for j in range (len(ls)):       
                for k in range (i+1):
                    result = ls[j][:k] + word[i] + ls[j][k:]
                    if result not in ls_:
                        ls_.append(result)
            
            ls = ls_
            
    return ls
    

if __name__ == "__main__":
    main()
