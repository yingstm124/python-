def main():
    assert(vowelCount("puzzle games")==4)
    assert(vowelCount("happy birthday")==3)
    assert(vowelCount("Recursive function")==7)

def vowelCount(word, count=0):
    word = word.lower()
    eng_ls = ["a","e","i","o","u"]

    if word[:] == "":
        return count
    
    if word[0] in eng_ls:
        count += 1
        
    return vowelCount(word[1:], count)

    
if __name__ == "__main__":
    main()
