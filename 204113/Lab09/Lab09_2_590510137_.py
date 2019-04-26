#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 09
# Problem 2
# 204113 Sec 001

import simpy


# 0 rock 1 paper 2 scissors

def main():
    x = 23
    score_player = 0
    score_com = 0
    drawing()
    i = 1 
    while i <= 3 :
        print("")
        player = int(input("PASS (key -1 for finish): "))
        if player == -1:
            print()
            print("GOODBYE!!!!!!!")
            return

        elif player <= 2:
            x = rand_sym(x)
            drawing_(x, player)
            
            player, com = check(player, x)
            score_player += player
            score_com += com

            draw_score(score_com, score_player)
            i += 1
        
        else:
            print("PASS AGAIN !!")
            continue

    print("-------------------------------")    

    if score_player > score_com:
        print("YOU WON")
    elif score_player == score_com:
        print("CAT GAME")
    else:
        print("YOU LOST")
    
    print("-------------------------------") 

def drawing_(com, player):
    ls = ["ROCK", "PAPER", "SCISSOR"]
    print()
    print("COMPUTER : {0}".format(ls[com]))
    print("YOU : {0}".format(ls[player]))

def draw_score(com_sc, player_sc):
    print("""__________________________________
|     COM      |    PLAYER1     |
|      {0}       |       {1}        |
|______________|________________|""".format(com_sc, player_sc))

    

def drawing():
    display = """[//////////////////////////////////////]
[/]¯¯¯¯¯¯¯¯¯¯[/]¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯[/]
[/]    TITLE [/] Rock Paper Scissors [/]
[/]    PASS  [/]   0    1      2     [/]
[/]__________[/]_____________________[/]
[//////////////////////////////////////]"""

    print(display)

def check(player, com):
    
    if player == com:
        return 0,0

    elif player==0 and com==2:
        return 1,0
    elif player==2 and com==1:
        return 1,0
    elif player==1 and com==0:
        return 1,0
    
    return 0,1

def rand_sym(x):
    a = 17
    c = 19
    m = 3
    xi = (a*(x)+c) % m

    return xi
    

if __name__ == "__main__":
    main()

