from random import *
import time

class Karte:


    #phase: 0=warte auf spieler, 1=verstearkung, 2=angriff, 3=bewegen
    phasetext = ["gegner wartet", "Verstaerkungsphase", "Angriffsphase", "Bewegungsphase"]

    #12 Provinzen(möglich fuer 2, 3 und 4 spieler: 6, 4, 3)

    #"knoten" : (nachbar1, nachbar2)
    knotennamen = {1 : "thessalonike", 2 : "olymp", 3:"athen", 4:"sparta", 5:"kreta", 6:"anatolien", 7:"naher osten", 8:"zypern", 9:"sinai", 10:"aegypten", 11:"libyen", 12:"byzanz"}
    knotenzahl = {1 : [2,12], 2 : [1,3,4], 3 : [2,4], 4 : [2,3,5], 5 : [4,6], 6 : [5,7,8,12], 7 : [6,8,9], 8 : [6,7], 9 : [7,10], 10 : [9,11], 11 : [10], 12 : [1,6]}

    # "info" : (anzEinheiten, BesitzerId)
    info = {1 : [1,2], 2 : [1,1], 3 : [1,1], 4 : [1,1], 5 : [1,1], 6 : [1,1], 7 : [1,1], 8 : [1,1], 9 : [1,1], 10 : [1,1], 11 : [1,1], 12 : [1,1]}


    def __init__(self, anz=4):
        self.anzSpieler = anz
        self.phase = 0
        self.spielerDran=0


    def nachbarn(self, knoten=1):
        return self.knotenzahl[knoten]#gibt tupel von knoten zurück


    def getProvInfo(self, knoten):
        return self.info[knoten]


    def nameVon(self, anz=1):
        return self.knotennamen[anz]

    def spielerAnReihe(self):
        return self.spielerDran + 1

    def getPhase(self):
        return (self.phasetext[self.phase], self.phase)

    def verstaerkeProv(self, numr):
        einheiten = self.info[numr][0]
        einheiten += 1
        self.info[numr][0] = einheiten


    def drueckeKnopf(self, numr, spielernr):
        #assert (isinstance(int, numr) and (numr<= 12 and numr > 0)), "Fehlerhafte Provinz gewaehlt"
        if(spielernr == self.spielerAnReihe()):
            #fuehre aktion des spielers aus, der gerade an reihe ist
            if self.phase == 1:
                pass
            elif self.phase == 2:
                pass
            elif self.phase == 3:
                pass

        if self.phase == 1:
            self.verstaerkeProv(numr)


        print(self.knotennamen[numr])


    def drueckeRunde(self):
        if(self.phase == 3):
            self.spielerDran = (self.spielerDran + 1) % self.anzSpieler
            print("Spieler", self.spielerDran, "ist an der Reihe")
        self.phase = (self.phase + 1) % 4
        print(self.phase, self.phasetext[self.phase])
        return self.phase


    def felderInitialisieren(self):
        if(self.anzSpieler == 2):
            sp=[6,6]
            frei = 12

            #belege feld zufaellig
            while(frei > 0):
                time.sleep(0.01)            #fuer zufallsgenerator
                besitzer = randint(1,2)
                if(sp[besitzer-1] > 0):
                    sp[besitzer-1] -= 1
                    self.info[frei][1] = besitzer
                    frei-=1

                #print("F2", frei,besitzer,self.info)

        if (self.anzSpieler == 3):
            sp=[4,4,4]
            frei = 12

            # belege feld zufaellig
            while (frei > 0):
                time.sleep(0.01)            #fuer zufallsgenerator
                besitzer = randint(1, 3)
                if (sp[besitzer-1] > 0):
                    sp[besitzer-1] -= 1
                    self.info[frei][1] = besitzer
                    frei -= 1
            pass
        if (self.anzSpieler == 4):
            sp=[3,3,3,3]
            frei = 12

            # belege feld zufaellig
            while (frei > 0):
                time.sleep(0.01)            #fuer zufallsgenerator
                besitzer = randint(1, 4)
                if (sp[besitzer-1] > 0):
                    sp[besitzer-1] -= 1
                    self.info[frei][1] = besitzer
                    frei -= 1
            pass