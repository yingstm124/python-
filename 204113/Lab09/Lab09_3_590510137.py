#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 09
# Problem 3
# 204113 Sec 001

import time
import datetime
import random

def main():
    today = datetime.datetime.now()
    x = int(today.microsecond)
    rand_a1 = qrand_dice(x)
    rand_a2 = qrand_dice(rand_a1)
    rand_b1 = qrand_dice(rand_a2)
    rand_b2 = qrand_dice(rand_b1)
    
    
    sum_a = rand_a1 + rand_a2
    draw_player("A")
    drawing(rand_a1, rand_a2, sum_a)

    sum_b = rand_b1 + rand_b2 
    draw_player("B")
    drawing(rand_b1, rand_b2, sum_b)


    if abs(sum_a - 8) < abs(sum_b - 8):
        result = "A won !!"
    elif abs(sum_a - 8) == abs(sum_b - 8):
        result = "cat game "
    else:
        result = "B won !!"

    for i in range (3):
        for j in range (32):
            if i==2 :
                print("-------------END----------------")
                break
            else:
                print("-",end="")
        print()

    finish(result)

def choosing_index(ls):
    num = random.randrange(0, len(ls))
    return num

def drawing(score_1, score_2, sum_score):
    pic = """_________________________________
|               |               |
|               |               |
|      {0}        |       {1}       |
|               |               |
|               |               |   
|_______________|_______________|""".format(score_1, score_2)

    print(pic)
    print()
    print("sum score : {0}".format(score_1 + score_2))
    print()

def draw_player(key):
    print("-----/////  PLAYER : {0} /////-----".format(key))

def finish(key):
    print("------->>> {0} <<<-------".format(key))

def qrand_dice(x):
    c = 1
    a = 186
    b = 7
    m = 6
    xi = (((a * (x**2)) + (b*x) + c) % m)
    xi += 1

    return xi


if __name__ == "__main__":
    main()