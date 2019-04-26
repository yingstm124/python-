#!/usr/bin/env python3
# sutimar pengpinij
# 590510137
# Lab 05
# Problem 5
# 204111 Sec 003
def main():
    year = int(input(""))
    print(zodiac_element(year))


def zodiac_element(year):
    zodiac = year%12
    element = year%10
    if element == 0 or element == 1:
        ans = "Metal"
    elif element == 2 or element == 3:
        ans = "Water"
    elif element == 4 or element == 5:
        ans = "Wood"
    elif element == 6 or element == 7:
        ans = "Fire"
    else: 
        ans = "Earth"
    
    if zodiac == 0 :
        ans1 = "Monkey"
    elif zodiac == 1:
        ans1 = "Rooster"
    elif zodiac == 2:
        ans1 = "Dog"
    elif zodiac == 3:
        ans1 = "Pig"
    elif zodiac == 4:
        ans1 = "Rat"
    elif zodiac == 5:
        ans1 = "Ox"
    elif zodiac == 6:
        ans1 = "Tiger"
    elif zodiac == 7:
        ans1 = "Rabbit"
    elif zodiac == 8:
        ans1 = "Dragon"
    elif zodiac == 9:
        ans1 = "Snake"
    elif zodiac == 10:
        ans1 = "Horse"
    else :
        ans1 = "Goat"

    a = ans + " " + ans1
    return a

if __name__=="__main__":
    main()
