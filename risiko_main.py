from random import *
from tkinter import *
import wuerfel
import karte








print("Starte wuerfel----------------------\n")
print("einmal wuerfeln =", wuerfel.wuerfeln())
print("zweimal wuerfeln =", wuerfel.wuerfeln(2))


map = karte.Karte()






def btn1func():
    w = map.drueckeRunde()

    if w == 0:
        butt1.config(image = imgstart)
    elif w == 1:
        butt1.config(image=imgverst)
    elif w == 2:
        butt1.config(image=imgangriff)
    elif w == 3:
        butt1.config(image=imgbewegen)


def btnprovfunc(zahl):
    map.drueckeKnopf(zahl)
    nachbarnZeigen(zahl)


def provblau():
    for x in range(13):
        if x != 0:
            butt[x].config(image = img2)


def nachbarnZeigen(provid):
    provblau()
    nbrn = map.nachbarn(provid)
    for x in range(len(nbrn)):
        butt[nbrn[x]].config(image = provrot)




##Start der Gui-initialisierung
breite = 720
hoehe =720

root = Tk()
theLabel = Label(root, text="Risiko")
theLabel.pack()


imgstart = PhotoImage(file="..\\karte\\start.png")
imgverst = PhotoImage(file="..\\karte\\verstaerkung.png")
imgangriff = PhotoImage(file="..\\karte\\angriff.png")
imgbewegen = PhotoImage(file="..\\karte\\bewegen.png")
gif1 = PhotoImage(file="..\\karte\\schiessen.gif")
img2 = PhotoImage(file="..\\karte\\provinz.png")
provrot = PhotoImage(file="..\\karte\\provinzrot.png")
butt1 = Button(root, image=imgstart, text="start", command= lambda : btn1func())

butt1.pack()

C = Canvas(root, height=hoehe, width=breite)

C.pack()

img = PhotoImage(file="..\\karte\\map_small.png")
C.create_image(0,0, anchor=NW, image=img)



#absolute platzierung der provinz-buttons
#########################################################################################
butt = [Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button()]
#provinz1
butt[1] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(1))
butt[1].place(x=135, y=180)
#provinz2
butt[2] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(2))
butt[2].place(x=70, y=220)
#provinz3
butt[3] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(3))
butt[3].place(x=135, y=280)
#provinz4
butt[4] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(4))
butt[4].place(x=120, y=350)
#provinz5
butt[5] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(5))
butt[5].place(x=250, y=480)
#provinz6
butt[6] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(6))
butt[6].place(x=450, y=250)
#provinz7
butt[7] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(7))
butt[7].place(x=650, y=400)
#provinz8
butt[8] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(8))
butt[8].place(x=500, y=405)
#provinz9
butt[9] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(9))
butt[9].place(x=550, y=610)
#provinz10
butt[10] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(10))
butt[10].place(x=400, y=650)
#provinz11
butt[11] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(11))
butt[11].place(x=200, y=650)
#provinz12
butt[12] = Button(root, image=img2, text="start", command= lambda : btnprovfunc(12))
butt[12].place(x=220, y=150)

root.mainloop()

