from random import *
from tkinter import *
from tkinter.messagebox import *
import sys
import time
import threading
import sqlite3
import socket


#---------------------------------------------------Singleplayer-GUI-----------------------------------------------------------
"""Gui hat keinen Zugriff auf Karte-Klasse"""

aktiverSpieler = 0          #vom server zugewiesen
letzteTruppen = 0
if(len(sys.argv) != 3):
    showerror("Fehler","nicht 2 Argumente angegeben!")
    exit(1)
ipaddr = sys.argv[1]
angriffvon = ""  # Hier wird Provinzid gespeichert, von der Angriff ausgeht
port = int(sys.argv[2])




def btn1func():
    #beende Spiel, wenn Spieler verloren hat
    provinit()

    labeltext.config(text=" ")
    r=1                                                                     #!Dummy
    w=0                                                                     #!Dummy

    # setze Farbe des Rundenbuttons
    if (r == 1):
        butt1.config(bg="lightblue")
    elif (r == 2):
        butt1.config(bg="yellow")
    elif (r == 3):
        butt1.config(bg="orange")
    elif (r == 4):
        butt1.config(bg="green")

    # waehle passendes Bild fuer Knopf
    if r != aktiverSpieler:
        if r == 1:
            butt1.config(image=imgstart)
        elif r == 2:
            butt1.config(image=imgstart2)
        elif r == 3:
            butt1.config(image=imgstart3)
        elif r == 4:
            butt1.config(image=imgstart4)
    elif w == 1:
        butt1.config(image=imgverst)
        labeltext.config(text="noch " + str(map.getVerstaerkung()) + " Einheiten platzieren")
    elif w == 2:
        labeltext.config(text="Angriff mit #Einheiten")
        butt1.config(image=imgangriff)
    elif w == 3:
        labeltext.config(text="Bewegen von #Einheiten")
        butt1.config(image=imgbewegen)

def btnprovfunc(zahl):
    provinit()


def provinit():
    for x in range(13):
        if x != 0:
            provinf = [0,0]                                                             #!Dummy
            if (provinf[1] == 1):
                butt[x].config(bg="lightblue")
            elif (provinf[1] == 2):
                butt[x].config(bg="yellow")
            elif (provinf[1] == 3):
                butt[x].config(bg="orange")
            elif (provinf[1] == 4):
                butt[x].config(bg="green")

def nachbarnZeigen(modus, provid):  # modus = 1|2: angriff oder bewegen; privid = Provinz
    pass

#thread des spieler
def idleplayer():
    while True:
        antwort = clientSocket.recv(1024).decode()
        if(antwort == 'exit'):
            print("Beende")
            exit(0)
        #clientSocket.send(nachricht.encode())


##Start der Gui-initialisierung
breite = 720
hoehe = 720

root = Tk()

kopf = Frame(root)
labeltext = Label(kopf, text=" ")
labeltext.pack(side=LEFT)
slider = Scale(kopf, from_=1, to=1, orient="horizontal")
slider.pack(side=LEFT)
kopf.pack()

imganfang = PhotoImage(file="karte\\anfang.png")
imgstart = PhotoImage(file="karte\\start.png")
imgstart2 = PhotoImage(file="karte\\start2.png")
imgstart3 = PhotoImage(file="karte\\start3.png")
imgstart4 = PhotoImage(file="karte\\start4.png")
imgverst = PhotoImage(file="karte\\verstaerkung.png")
imgangriff = PhotoImage(file="karte\\angriff.png")
imgbewegen = PhotoImage(file="karte\\bewegen.png")
gif1 = PhotoImage(file="karte\\schiessen.gif")
butt1 = Button(root, image=imganfang, text="start", command=lambda: btn1func())
butt1.pack()

C = Canvas(root, height=hoehe, width=breite)


img = PhotoImage(file="karte\\map_small.png")
C.create_image(0, 0, anchor=NW, image=img)
C.pack()

yoffset = 20
# absolute platzierung der provinz-buttons
#########################################################################################
butt = [Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(),
        Button(), Button(), Button()]
# provinz1
butt[1] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(1))
butt[1].place(x=135, y=180+yoffset)
# provinz2
butt[2] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(2))
butt[2].place(x=70, y=220+yoffset)
# provinz3
butt[3] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(3))
butt[3].place(x=135, y=280+yoffset)
# provinz4
butt[4] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(4))
butt[4].place(x=120, y=350+yoffset)
# provinz5
butt[5] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(5))
butt[5].place(x=250, y=480+yoffset)
# provinz6
butt[6] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(6))
butt[6].place(x=450, y=250+yoffset)
# provinz7
butt[7] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(7))
butt[7].place(x=650, y=400+yoffset)
# provinz8
butt[8] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(8))
butt[8].place(x=500, y=405+yoffset)
# provinz9
butt[9] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(9))
butt[9].place(x=550, y=610+yoffset)
# provinz10
butt[10] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(10))
butt[10].place(x=400, y=650+yoffset)
# provinz11
butt[11] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(11))
butt[11].place(x=200, y=650+yoffset)
# provinz12
butt[12] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(12))
butt[12].place(x=220, y=150+yoffset)

provinit()

#Server beitreten
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    clientSocket.connect((ipaddr,port))
except socket.gaierror:
    showerror("Fehler", "Server offline oder Adresse falsch!")
    exit(3)
except ConnectionRefusedError:
    showerror("Fehler", "falscher Port oder Server offline!")
nachricht = "liketojoin"
clientSocket.send(nachricht.encode())
antwort = clientSocket.recv(1024).decode()
if(len(antwort) == 4 and antwort[0] == 'o' and antwort[1] == 'k'):
    aktiverSpieler = int(antwort[3])
    print("SPIELER =",aktiverSpieler)
    root.title("Risiko Multiplayer, als Spieler " + str(aktiverSpieler) + " beigetreten")
    threading._start_new_thread(idleplayer,())
else:
    showerror("Fehler", "Server voll!")
    exit(2)

root.mainloop()