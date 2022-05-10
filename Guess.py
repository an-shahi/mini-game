import tkinter as tk
from tkinter import *
import random

global no
global score
root = Tk()
root.title("Guess Game")
root.geometry('600x400')
root.configure(bg="light green")
no = random.randint(1, 100)
score = 0
choice = IntVar()


def comp():
    global score
    if no < choice.get():
        Label1 = Label(root, text=" Guess a lower Number ",
                       relief=RIDGE, font=('Roboto', 15))
        Label1.place(relx=0.5, rely=0.6, anchor=CENTER)
        score += 1

    elif no > choice.get():
        Label2 = Label(root, text=" Guess a Higher Number",
                       relief=RIDGE, font=('Roboto', 15), )
        Label2.place(relx=0.5, rely=0.6, anchor=CENTER)
        score += 1
    else:
        Label3 = Label(root, text="Damn🔥🔥.Right Answer!!",
                       relief=RIDGE, font=('Roboto', 15))
        Label3.place(relx=0.5, rely=0.6, anchor=CENTER)
        Label5 = Label(root, text=score,
                       relief=RIDGE, font=('Roboto', 15))
        Label5.place(relx=0.57, rely=0.5, anchor=CENTER)


def resart():
    global no
    global score
    no = random.randint(1, 100)
    score = 0
    Label6 = Label(root, text=score,
                   relief=RIDGE, font=('Roboto', 15))
    Label6.place(relx=0.55, rely=0.5, anchor=CENTER)
    return


Labelhead = Label(root, text="Enter any Number between 1 to 100 ", relief=RIDGE, font=('Roboto', 20))
Labelhead.place(relx=0.5, rely=0.05, anchor=CENTER)

Label4 = Label(root, text="Score = ",
               relief=RIDGE, font=('Roboto', 15))
Label4.place(relx=0.5, rely=0.5, anchor=CENTER)

ent1 = Entry(root, textvariable=choice, width=3,
             font=('Roboto', 50), relief=GROOVE)
ent1.place(relx=0.5, rely=0.275, anchor=CENTER)

myButton1 = Button(root, text="GUESS", padx=35, pady=15, command=comp)
myButton1.place(relx=0.5, rely=0.8, anchor=CENTER)

myButton2 = Button(root, text="Quit", padx=45, pady=15, command=root.destroy)
myButton2.place(relx=0.75, rely=0.8, anchor=CENTER)

myButton3 = Button(root, text="Play Again", padx=35, pady=15, command=resart)
myButton3.place(relx=0.25, rely=0.8, anchor=CENTER)

root.mainloop()
