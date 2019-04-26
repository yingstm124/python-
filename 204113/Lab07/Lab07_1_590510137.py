#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 07
# Problem 1
# 204113 Sec 001

def main():
    word = 'bEe'
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
