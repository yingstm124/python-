import random

def ls_create(length):
    ls_ = []
    for i in range (length):
        ls_.append("_")
    return ls_

def display_block_line(length, keyword):
    for i in range (length):
        print("_",end=" ")
    print(" : {0}".format(keyword))

def end_game():    
    print("goodbye")

def get_ready():
    incorrect = False
    while not incorrect:
        ready = str(input("Are you ready (y/n): "))
        ready.islower()
        if ready == "y":
            return True
        elif ready == "n":
            return False
        else:
            print("please key again")

def win():
    print("you win!")

def print_ls(ls_):
    for i in range (len(ls_)):
        print(ls_[i],end=" ")
    print("")

def print_guess_word():
    global length_word, word_random_ls
    alphabet_ls = ["a","b","c","d","e","f","g","h","i"
                    "j","k","l","m","n","o","p","q","u",
                    "r","s","t","u","v","w","x","y","z"]

    ls_check = []
 
    for i in range (length_word):
    
        while True:
            index_word = random.randint(0,length_word - 1 )
            if word_random_ls[index_word] not in ls_check:
                break

        ls_check.append(word_random_ls[index_word])
        print(word_random_ls[index_word],end=" ")

        index = random.randint(0,len(alphabet_ls) - 1)
        print(alphabet_ls[index],end=" ")

    print("")

def guest():
    global word_random, word_random_ls, length_word, ls_word, key_random
    
    lost = False 
    full = False
    j = 0
    
    display_block_line(length_word ,key_random)
    print_guess_word()
    while not full or lost:
        
        guest_char = str(input("key only one character: "))
        if len(guest_char) != 1:
            print("only one!!!!!!!")
        else:
            found = False
            for i in range (len(word_random)):
                if word_random[i] == guest_char:
                    if ls_word[i] == "_":
                        ls_word[i] = guest_char
                        found = True
                    if found == True:
                        j += 1
                        break

            if not found:
                print("-----------------------------------------")
                print_guess_word()
                print_ls(ls_word)
                print("incorrect")
            else:
                print("-----------------------------------------")
                print_guess_word()
                print_ls(ls_word)

            if j == length_word:
                win()
                full = True
        
        

def process():
    global word_random, word_random_ls, length_word, ls_word

    ready = get_ready()
    if ready == False:
        end_game()
    else:
        guest()
    
  
##############################################################################

# global
word = {"animal":["ant"],"fruit":["banana"]}

key_random = random.choice(list(word.keys()))
index = random.randint(0,len(word[key_random])-1)
word_random = word[key_random][index]
word_random_ls = list(word_random)
length_word = len(word_random)
ls_word = ls_create(length_word)

# get start for process
process()
    
    




    

