from random import *
import time

class Karte:


    #phase: 0=warte auf spieler, 1=verstearkung, 2=angriff, 3=bewegen
    phasetext = ["gegner wartet", "Verstaerkungsphase", "Angriffsphase", "Bewegungsphase"]

    #12 Provinzen(möglich fuer 2, 3 und 4 spieler: 6, 4, 3)

    #"knoten" : (nachbar1, nachbar2)
    knotennamen = {1 : "thessalonike", 2 : "olymp", 3:"athen", 4:"sparta", 5:"kreta", 6:"anatolien", 7:"naher osten", 8:"zypern", 9:"sinai", 10:"aegypten", 11:"libyen", 12:"byzanz"}
    knotenzahl = {1 : [2,12], 2 : [1,3,4], 3 : [2,4], 4 : [2,3,5], 5 : [4,6], 6 : [5,7,8,12], 7 : [6,8,9], 8 : [6,7], 9 : [7,10], 10 : [9,11], 11 : [10], 12 : [1,6]}
    land = {0 : ["Griechenland",0,2], 1 : ["Afrika",0,1], 2 : ["Kleinasien",0,1]}       #name, besitzer(0 == keiner), anzahl einheitenverstaerkung

    # "info" : (anzEinheiten, BesitzerId)
    info = {1 : [1,2], 2 : [1,1], 3 : [1,1], 4 : [1,1], 5 : [1,1], 6 : [1,1], 7 : [1,1], 8 : [1,1], 9 : [1,1], 10 : [1,1], 11 : [1,1], 12 : [1,1]}


    #Konstruktor
    def __init__(self, anz=2):
        self.anzSpieler = anz
        self.phase = 0
        self.spielerDran=0
        self.verstaerkung=0
        self.provAuswahl=0


    #gibt nachbarn von angegebener provinz als liste zurueck
    def nachbarn(self, knoten=1):
        return self.knotenzahl[knoten]


    #gibt provinzinfo-liste der angegebenen Provinz zurueck
    def getProvInfo(self, knoten):
        return self.info[knoten]


    #gibt Karte zurueck
    def getMap(self):
        return self.info


    #gibt den Besitzer der engagabenen Provinz zurueck
    def getBesitzer(self, knoten):
        return self.info[knoten][1]


    #gibt den Namen der angegebenen Provinz zurueck
    def nameVon(self, anz=1):
        return self.knotennamen[anz]


    #gibt den Spieler zurueck, der gerade an der Reihe ist
    def spielerAnReihe(self):
        return self.spielerDran + 1


    #gibt die moegliche Anzahl an Verstaerkungs-Einheiten des angegebenen Spielers zurueck
    def berechneVerstaerkung(self,spieler):
        provinbesitz=0
        for prov in self.info:
            if(prov[1] == spieler):
                provinbesitz+=1

        verst = round(provinbesitz/3)

        for l in self.land:
            if l[1] == spieler:
                verst += l[2]

        return verst


    #gibt die aktuelle Phase zurueck
    def getPhase(self):
        return (self.phasetext[self.phase], self.phase)


    #erhoehe die Anzahl der Einheiten der angegebenen Provinz um 1
    def verstaerkeProv(self, numr, anzahl=1):
        self.info[numr][0] += anzahl


    #bewege 'anzahl' Einheiten von Provinz'von' nach Provinz'nach'
    def bewege(self,von,nach,anzahl=1):
        if(self.info[von][0] > anzahl):
            self.info[von][0] -= anzahl
            self.info[nach][0] += anzahl


    #TODO 'spieler' greift von Provinz 'von' mit 'anz' Einheiten Provinz 'nach' an
    def angreifen(self, von, nach, anzahl, spieler):
        if(self.info[von][0] > anzahl):
            self.info[von][0] -= anzahl
            self.info[nach][1] = spieler
            self.info[nach][0] = anzahl


    #TODO
    def verschieben(self, provnr):
        pass


    #gibt zurueck, ob die angegebene Provinz dem Spieler gehoert
    def eigeneProvinz(self, provnr, spielernr):
        if(self.info[provnr][1] == spielernr):
            return True
        else:
            return False



    #schnittstelle der Provinzauswahl
    def drueckeKnopf(self, provnumr, spielernr):
        #assert (isinstance(int, numr) and (numr<= 12 and numr > 0)), "Fehlerhafte Provinz gewaehlt"
        if(spielernr == self.spielerAnReihe()):
            #fuehre aktion des spielers aus, der gerade an reihe ist
            if self.phase == 1 and self.info[provnumr][1] == self.spielerAnReihe():
                #self.verstaerkung = self.berechneVerstaerkung(spielernr)   #wird zu beginn einer runde aufgerufen, nachdem der/die gegner fertig ist/sind
                self.verstaerkeProv(provnumr)
            elif self.phase == 2:
                if((not self.eigeneProvinz(provnumr, spielernr)) and self.provAuswahl != 0 and provnumr in self.knotenzahl[self.provAuswahl]):
                    self.angreifen(self.provAuswahl, provnumr, 1, spielernr)
                    self.provAuswahl = 0
                    return ["angriff", provnumr]
                elif(self.eigeneProvinz(provnumr, spielernr)):
                    self.provAuswahl = provnumr
            elif self.phase == 3:
                if ((self.eigeneProvinz(provnumr, spielernr)) and self.provAuswahl != 0 and provnumr in self.knotenzahl[self.provAuswahl]):
                    self.bewege(self.provAuswahl,provnumr)
                    self.provAuswahl = 0
                    return ["bewegen", provnumr]
                elif (self.eigeneProvinz(provnumr, spielernr)):
                    self.provAuswahl = provnumr

            if (self.provAuswahl == 0):
                self.provAuswahl = provnumr
        else:
            return ["spieler", self.spielerAnReihe(), "dran"]

        #if self.phase == 1 and self.spielerDran+1 == spielernr and self.info[provnumr][1] == spielernr:
        #    self.verstaerkeProv(provnumr)

        print(self.knotennamen[provnumr])
        return None


    #veraendert die Phase, evtl kommt ein neuer Spieler dran
    def drueckeRunde(self):
        if(self.phase == 3):
            self.spielerDran = (self.spielerDran + 1) % self.anzSpieler
            print("Spieler", self.spielerAnReihe(), "ist an der Reihe")
        self.phase = (self.phase + 1) % 4
        print(self.phase, self.phasetext[self.phase])
        self.provAuswahl=0
        return self.phase


    #legt die startprovinzen fest
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