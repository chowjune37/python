from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb
import random

def guess_number():
    number = int(random.random()*100)
    root = Tk()
    w = Label(root,text = 'title')
    w.pack()

    mb.showinfo("welcome","guess begin!")

    while(1):
        guess = dl.askinteger('number','input')
        if(guess == number):
            mb.showinfo('m','you win!!!')
            break
        elif(guess > number):
            mb.showinfo('m','too big')
        else:
            mb.showinfo('m','too small')

if __name__ == '__main__':
    guess_number()
