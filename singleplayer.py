from random import *
from tkinter import *
from tkinter.messagebox import *
import sys
import karte


#---------------------------------------------------Singleplayer-GUI-----------------------------------------------------------
"""Gui hat direkten Zugriff auf Karte-Klasse"""

map = karte.Karte(int(sys.argv[1]))
map.felderInitialisieren()
angriffvon = ""  # Hier wird Provinzid gespeichert, von der Angriff ausgeht
aktiverSpieler = int(sys.argv[2])



def btn1func():
    w = map.drueckeRunde()
    r = map.spielerAnReihe()
    provinit()

    labeltext.config(text=" ")

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
        butt1.config(image=imgangriff)
    elif w == 3:
        butt1.config(image=imgbewegen)

def btnprovfunc(zahl):
    provinit()

    rueckgabe = map.drueckeKnopf(zahl, aktiverSpieler)
    if (rueckgabe == None):

        print("Phase:", map.getPhase())

        if (map.getBesitzer(zahl) == aktiverSpieler):
            if (map.getPhase()[1] == 2):
                nachbarnZeigen(1, zahl)
            elif (map.getPhase()[1] == 3):
                nachbarnZeigen(2, zahl)
            elif (map.getPhase()[1] == 1):
                labeltext.config(text="noch " + str(map.getVerstaerkung()) + " Einheiten platzieren")
                provinit()
    elif (rueckgabe[0] == "angriff"):
        msg = "Schlacht von " + map.nameVon(zahl)
        print(msg)
        showinfo("Angriff", msg)
        provinit()
        if(map.getAktiveSpieler() == 1):
            print("Spiel zuende") #TODO: geht noch nicht
            showinfo("Ende","Spieler" + str(map.spielerAnReihe()) + "hat gewonnen!")
    elif (rueckgabe[0] == "bewegen"):
        provinit()

def provinit():
    for x in range(13):
        if x != 0:
            butt[x].config(text=map.getProvInfo(x)[0])
            provinf = map.getProvInfo(x)
            if (provinf[1] == 1):
                butt[x].config(bg="lightblue")
            elif (provinf[1] == 2):
                butt[x].config(bg="yellow")
            elif (provinf[1] == 3):
                butt[x].config(bg="orange")
            elif (provinf[1] == 4):
                butt[x].config(bg="green")

def nachbarnZeigen(modus, provid):  # modus = 1|2: angriff oder bewegen; privid = Provinz
    angriffvon = provid
    nbrn = map.nachbarn(provid)
    for x in range(len(nbrn)):
        if (modus == 1):
            if (map.getProvInfo(provid)[1] != map.getProvInfo(nbrn[x])[1]):
                butt[nbrn[x]].config(bg="red")
        elif (modus == 2):
            if (map.getProvInfo(provid)[1] == map.getProvInfo(nbrn[x])[1]):
                butt[nbrn[x]].config(bg="black")


##Start der Gui-initialisierung
breite = 720
hoehe = 720

root = Tk()


labeltext = Label(root, text=" ")
labeltext.pack()

imganfang = PhotoImage(file="..\\karte\\anfang.png")
imgstart = PhotoImage(file="..\\karte\\start.png")
imgstart2 = PhotoImage(file="..\\karte\\start2.png")
imgstart3 = PhotoImage(file="..\\karte\\start3.png")
imgstart4 = PhotoImage(file="..\\karte\\start4.png")
imgverst = PhotoImage(file="..\\karte\\verstaerkung.png")
imgangriff = PhotoImage(file="..\\karte\\angriff.png")
imgbewegen = PhotoImage(file="..\\karte\\bewegen.png")
gif1 = PhotoImage(file="..\\karte\\schiessen.gif")
butt1 = Button(root, image=imganfang, text="start", command=lambda: btn1func())

butt1.pack()

C = Canvas(root, height=hoehe, width=breite)


img = PhotoImage(file="..\\karte\\map_small.png")
C.create_image(0, 0, anchor=NW, image=img)
C.pack()

# absolute platzierung der provinz-buttons
#########################################################################################
butt = [Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(),
        Button(), Button(), Button()]
# provinz1
butt[1] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(1))
butt[1].place(x=135, y=180)
# provinz2
butt[2] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(2))
butt[2].place(x=70, y=220)
# provinz3
butt[3] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(3))
butt[3].place(x=135, y=280)
# provinz4
butt[4] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(4))
butt[4].place(x=120, y=350)
# provinz5
butt[5] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(5))
butt[5].place(x=250, y=480)
# provinz6
butt[6] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(6))
butt[6].place(x=450, y=250)
# provinz7
butt[7] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(7))
butt[7].place(x=650, y=400)
# provinz8
butt[8] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(8))
butt[8].place(x=500, y=405)
# provinz9
butt[9] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(9))
butt[9].place(x=550, y=610)
# provinz10
butt[10] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(10))
butt[10].place(x=400, y=650)
# provinz11
butt[11] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(11))
butt[11].place(x=200, y=650)
# provinz12
butt[12] = Button(root, bg="blue", text="1", command=lambda: btnprovfunc(12))
butt[12].place(x=220, y=150)

provinit()
root.mainloop()