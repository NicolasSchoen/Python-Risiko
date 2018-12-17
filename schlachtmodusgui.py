from random import *
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
import wuerfel

def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    label = tk.Label(self, text="Schlachtmodus")
    label.pack(side="top", fill="x", pady=10)
    button2 = tk.Button(self, text="Angreifen", command=lambda: self.btn1func())
    button1 = tk.Button(self, text="Rueckzug", command=lambda: self.btn2func())




def btn1func(self):
    wuerfel.wuerfeln()


#def btn2func(self):



#Start der Gui-initialisierung#
breite = 480
hoehe = 480

root = Tk()

kopf = Frame(root)
labeltext = Label(kopf, text=" ")
labeltext.pack(side=LEFT)
slider = Scale(kopf, from_=1, to=1, orient="horizontal")
slider.pack(side=LEFT)
kopf.pack()

#imgwuerfel = tk.PhotoImage(file="..\\schlachtmodus\\wuerfel.png")
#imgsoldat = tk.PhotoImage(file="..\\schlachtmodus\\soldat.png")

button1 = Button(root, text="Angreifen", command=lambda: btn1func())
#b
button1.pack()

C = Canvas(root, height=hoehe, width=breite)




root.mainloop()