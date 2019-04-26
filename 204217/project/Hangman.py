from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import random
import sys

class Display():
    def __init__(self, win, chance):
        self.screen = win
        self.chance = chance 
        self.display()
    def display(self):
        global word_r,chance
        self.screen.title("Hangman Game")
        top = Label(self.screen, text="Hangman Game", font=("",30), pady=12).pack()
        Label(self.screen, text="GUESS : Friut", pady=5, fg="red").pack()
        # self.hanger()
        gameplay(self.screen)
        
        
class gameplay():
    def __init__(self, win):
        global word_r, chance

        self.chance = chance
        self.screen = win
        self.ls = list()
        self.word = word_r

        print(self.word)
        print(self.chance)

        self.temp = self.hanger()

        self.c = Canvas(self.screen, width=400, height=300)
        self.c1 = Canvas(self.screen, width=400, height=200)
        
        self.create_gw(self.c1)
        self.c1.pack()

        self.create_k(self.c)
        self.c.pack()
        
    
    def guess_word(self):
        self.ls = []
        for i in range (len(word_r)):
            l = Label(self.c, text="_")
            l.grid(row=0, column=i)
            self.ls.append(l)
    
    def create_gw(self,c):
        global word_r1
        self.ls = []
        for i in range (len(self.word)):
            if self.word[i] == "#":
                l = Label(c, text=word_r1[i])
                l.grid(row=0, column=i)
            else:
                l = Label(c, text="_")
                l.grid(row=0, column=i)
            self.ls.append(l)
    
                
    def hanger(self):
      c = Canvas(self.screen, width=400, height=300)
      c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
      c.create_line(140, 3, 250, 3, width=10)
      c.create_line(250, 0, 250, 280, width=6)
      c.create_line(130, 280, 310, 280, width=6)
      c.pack()

      return c
    
    def head(self,c):
        c.create_oval(110,40,170,100)
    
    def body(self,c):
        c.create_line(140,100,140,190)

    def leftarm(self,c):
        c.create_line(140,110,115,150)

    def rightarm(self,c):
        c.create_line(140,110,165,150)
    
    def leftleg(self,c):
        c.create_line(140,190,165,240)

    def rightleg(self,c):
        c.create_line(140,190,115,240)
    
    def exitApp(self):
        sys.exit()

    def change_pic(self, chance):
        global word, image_win, image_lost
        
        finish = False
        for i in range (len(self.word)):
            if self.word[i] != "#" and i < (len(self.word)-1):
                finish = False
                break

            elif self.word[i] == "#":
                finish = True        

        if finish == True:
            self.screen.destroy()
            win = Tk()
            win.geometry("200x200")
            Label(win, text="End game", font=("","45"), pady=30).pack()
            Label(win, text="YOU WIN!", font=("","18"),pady=5).pack()
            q = Button(win, text="Quit!", command=self.exitApp).pack()
            mainloop()

        if chance == 5:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1

            
        elif chance == 4:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            self.body(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1

        elif chance == 3:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            self.body(c)
            self.leftarm(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1

        elif chance == 2:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            self.body(c)
            self.leftarm(c)
            self.rightarm(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1
        
        elif chance == 1:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            self.body(c)
            self.leftarm(c)
            self.rightarm(c)
            self.leftleg(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1
        
        elif chance == 0:
            c = Canvas(self.screen, width=400, height=300)
            c1 = Canvas(self.screen, width=400, height=200)
            # ls = [self.head(c), self.body(c), self.leftarm(c), self.rightarm(c), self.leftleg(c), self.rightleg(c)]
            c.create_line(140, 3, 140, 40, dash=(4, 2), width=2)
            self.head(c)
            self.body(c)
            self.leftarm(c)
            self.rightarm(c)
            self.leftleg(c)
            self.rightleg(c)
            c.create_line(140, 3, 250, 3, width=10)
            c.create_line(250, 0, 250, 280, width=6)
            c.create_line(130, 280, 310, 280, width=6)
            c.pack()
            self.create_gw(c1)
            self.create_k(c1)
            self.c = c
            self.c1 = c1
        # lost! game
        else:
            self.screen.destroy()
            win = Tk()
            win.geometry("200x200")
            Label(win, text="End game", font=("","45"), pady=30).pack()
            Label(win, text="YOU LOST!", font=("","18"),pady=5).pack()
            q = Button(win, text="Quit!", command=self.exitApp).pack()
            mainloop()
            return 
        

    def update_pic(self):
        print(self.chance)
        self.temp.destroy()
        self.c.destroy()
        self.c1.destroy()
        
        self.change_pic(self.chance)
        

    def chance_cal(self):
        self.chance -= 1
        self.update_pic()
        
    def buttonfunc(self, key):
        found = False
        for i in range (len(self.ls)):
            if key in self.word and self.ls[i]["text"] == "_":
                if key == self.word[i]:
                    temp = list(self.word)
                    temp[i] = "#"
                    self.word = "".join(temp)
                    print(self.word)
                    self.ls[i].config(text=key)
                    found = True
                    break
            if found == False and i == len(self.ls)-1:
                self.chance_cal()
            

    def create_k(self, c):
        Button(c, text=" ", width=2, ).grid(row=1, column=0)
        Button(c, text="q", width=2, command=lambda:self.buttonfunc("q")).grid(row=1, column=1)
        Button(c, text="w", width=2, command=lambda:self.buttonfunc("w")).grid(row=1, column=2)
        Button(c, text="e", width=2, command=lambda:self.buttonfunc("e")).grid(row=1, column=3)
        Button(c, text="r", width=2, command=lambda:self.buttonfunc("r")).grid(row=1, column=4)
        Button(c, text="t", width=2, command=lambda:self.buttonfunc("t")).grid(row=1, column=5)
        Button(c, text="y", width=2, command=lambda:self.buttonfunc("y")).grid(row=1, column=6)
        Button(c, text="u", width=2, command=lambda:self.buttonfunc("u")).grid(row=1, column=7)
        Button(c, text="l", width=2, command=lambda:self.buttonfunc("l")).grid(row=1, column=8)
        Button(c, text="o", width=2, command=lambda:self.buttonfunc("o")).grid(row=1, column=9)
        Button(c, text="p", width=2, command=lambda:self.buttonfunc("p")).grid(row=1, column=10)

        Button(c, text="a", width=2, command=lambda:self.buttonfunc("a")).grid(row=2, column=1)
        Button(c, text="s", width=2, command=lambda:self.buttonfunc("s")).grid(row=2, column=2)
        Button(c, text="d", width=2, command=lambda:self.buttonfunc("d")).grid(row=2, column=3)
        Button(c, text="f", width=2, command=lambda:self.buttonfunc("f")).grid(row=2, column=4)
        Button(c, text="g", width=2, command=lambda:self.buttonfunc("g")).grid(row=2, column=5)
        Button(c, text="h", width=2, command=lambda:self.buttonfunc("h")).grid(row=2, column=6)
        Button(c, text="j", width=2, command=lambda:self.buttonfunc("j")).grid(row=2, column=7)
        Button(c, text="k", width=2, command=lambda:self.buttonfunc("k")).grid(row=2, column=8)
        Button(c, text="i", width=2, command=lambda:self.buttonfunc("i")).grid(row=2, column=9)
            
        Button(c, text="z", width=2, command=lambda:self.buttonfunc("z")).grid(row=3, column=2)
        Button(c, text="x", width=2, command=lambda:self.buttonfunc("x")).grid(row=3, column=3)
        Button(c, text="c", width=2, command=lambda:self.buttonfunc("c")).grid(row=3, column=4)
        Button(c, text="v", width=2, command=lambda:self.buttonfunc("v")).grid(row=3, column=5)
        Button(c, text="b", width=2, command=lambda:self.buttonfunc("b")).grid(row=3, column=6)
        Button(c, text="n", width=2, command=lambda:self.buttonfunc("n")).grid(row=3, column=7)
        Button(c, text="m", width=2, command=lambda:self.buttonfunc("m")).grid(row=3, column=8)
        
        c.pack()



win = Tk()
win.geometry("400x550")
chance = 6

image_lost = PhotoImage(file="/Users/sutimar/mywork/204217/project/lost.png")
#image_win = PhotoImage(file="/Users/sutimar/mywork/204217/project/win.jpg")

word = ["Apple","Banana","Strawberry","Pineapple","Papaya","Orange","Grape","Coconut","Cherry","Blueberry","Kiwi","Longan","Mangoteen","Pear","Raspberry","Cherry","Lychee"]
word_r = random.choice(word).lower()
word_r1 = word_r

Display(win, chance)

mainloop()