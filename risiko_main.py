from random import *
from tkinter import *
import wuerfel





class Karte:

    anzSpieler=2

    #12 Provinzen(möglich fuer 2, 3 und 4 spieler: 6, 4, 3)

    #"knoten" : (nachbar1, nachbar2)
    knotennamen = {1 : "provinz1", 2 : "provinz2", 3:"provinz3", 4:"provinz4", 5:"provinz5", 6:"provinz6", 7:"provinz7", 8:"provinz8", 9:"provinz9", 10:"provinz10", 11:"provinz11", 12:"provinz12"}
    knotenzahl = {1 : (2,3,8), 2 : (1,3,9), 3 : (1,2,4,5,6), 4 : (3,10,11), 5 : (3,6,11,12), 6 : (3,5,7,8), 7 : (6), 8 : (1,6), 9 : (2,10), 10 : (4,9,11), 11 : (4,5,10,12), 12 : (5,11)}

    # "info" : (anzEinheiten, BesitzerId)
    info = {"provinz1" : (5,2), "provinz2" : (2,1)}


    def __init__(self, anz=2):
        anzSpieler = anz


    def nachbarn(self, knoten=1):
        return self.knotenzahl[knoten]#gibt tupel von knoten zurück

    def nameVon(self, anz=1):
        return self.knotennamen[anz]

    def felderInitialisieren(self):
        if(self.anzSpieler == 2):
            sp=(6,6)
            frei = 12

            #belege feld zufaellig
            while(frei > 0):
                besitzer = randint(1,2)
                if(sp[besitzer] > 0):
                    sp[besitzer] -= sp[besitzer]
                    self.info[frei] = (1, besitzer)
                    frei-=1

            pass
        if (self.anzSpieler == 3):
            sp=(4,4,4)
            frei = 12

            # belege feld zufaellig
            while (frei > 0):
                besitzer = randint(1, 3)
                if (sp[besitzer] > 0):
                    sp[besitzer] -= sp[besitzer]
                    self.info[frei] = (1, besitzer)
                    frei -= 1
            pass
        if (self.anzSpieler == 4):
            sp=(3,3,3,3)
            frei = 12

            # belege feld zufaellig
            while (frei > 0):
                besitzer = randint(1, 4)
                if (sp[besitzer] > 0):
                    sp[besitzer] -= sp[besitzer]
                    self.info[frei] = (1, besitzer)
                    frei -= 1
            pass


print("Starte wuerfel----------------------\n")
print("einmal wuerfeln =", wuerfel.wuerfeln())
print("zweimal wuerfeln =", wuerfel.wuerfeln(2))


##Start der Gui-initialisierung
breite = 720
hoehe =720

root = Tk()
theLabel = Label(root, text="Risiko")
theLabel.pack()

C = Canvas(root, height=hoehe, width=breite)

C.pack()

img = PhotoImage(file="..\\karte\\map_small.png")
C.create_image(0,0, anchor=NW, image=img)

root.mainloop()

