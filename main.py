
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

TOWERSPACE = [0, 0, 0]
COIN = 0
TOWERPRICE = 0
master = Tk()
master.title("S2K Game")
master.geometry("400x400")



def buyspace():
    global COIN
    if COIN >= 10:
        TOWERSPACE.append(0)
        spaceLabel.config(text="Your Space\n" + str(TOWERSPACE))
        COIN -= 10
        coinLabel.config(text="Coin: " + str(COIN))
    else:
        messagebox.showerror("İşlem Gerçekleşmedi","Yeterli Paran Yok")


def coinadd():
    global COIN
    COIN += 1
    coinLabel.config(text="Coin: " + str(COIN))

def addtower():
    global COIN, TOWERPRICE
    try:
        if COIN >= TOWERPRICE:
            index = TOWERSPACE.index(0)
            TOWERSPACE[index] = 1
            spaceLabel.config(text="Your Space\n" + str(TOWERSPACE))
            COIN -= TOWERPRICE
            coinLabel.config(text="Coin: " + str(COIN))
            TOWERPRICE += 5
            towerAddBtn.config(text="Add Tower (-"+str(TOWERPRICE)+" Coin)")
        else:
            messagebox.showerror("İşlem Gerçekleşmedi", "Yeterli Paran Yok")
    except ValueError:
        messagebox.showerror("İşlem Gerçekleşmedi", "Kule Kurmak İçin Boş Alan Yok")

def merge():
    for i in TOWERSPACE:
        if i == 0:
            continue
        else:
            try:
                index = TOWERSPACE.index(i)
                index2 = TOWERSPACE.index(i, index + 1)
                TOWERSPACE[index] = i + 1
                TOWERSPACE[index2] = 0
                spaceLabel.config(text="Your Space\n" + str(TOWERSPACE))
            except Exception:
                continue

gameNameLabel = Label(master, text="Merge Game", background="red", justify="center", anchor="center")
gameNameLabel.pack(pady=10, fill=tkinter.X)
spaceLabel = Label(master, text="Your Space\n" + str(TOWERSPACE), background="yellow", justify="center",
                   anchor="center")
spaceLabel.pack(pady=5, fill=tkinter.X)
coinLabel = Label(master, text="Coin: " + str(COIN), anchor="center")
coinLabel.pack(pady=5, fill=tkinter.X)
btn = Button(master, text="Buy Space (-10 Coin)", command=buyspace)
btn.pack(pady=10)
coinAddBtn = Button(master, text="Earn Money(+1 Coin)", command=coinadd)
coinAddBtn.pack(pady=10)
towerAddBtn = Button(master, text="Add Tower (-"+str(TOWERPRICE)+" Coin)", command=addtower)
towerAddBtn.pack(pady=10)
mergeBtn = Button(master, text="Merge Tower", command=merge)
mergeBtn.pack(pady=10)
mainloop()

