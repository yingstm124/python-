#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 2
# 204113 Sec 001

def main():
    # test vowelcount
    assert(vowelCount("puzzle games")==4)
    assert(vowelCount("happy birthday")==3)
    assert(vowelCount("Recursive function")==7)
    print("vowel count is pass")

def vowelCount(word, count=0):
    # convert to lower string every word
    word = word.lower()
    # list of vowel
    eng_ls = ["a","e","i","o","u"]
    # base case when string " "
    if word[:] == "":
        return count
    # check vowel with the first string  
    if word[0] in eng_ls:
        count += 1
        
    return vowelCount(word[1:], count)

    
if __name__ == "__main__":
    main()
