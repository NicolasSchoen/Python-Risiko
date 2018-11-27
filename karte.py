from random import *
import time
import schlacht

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

    spielergueltig = [False, False, False, False]


    #Konstruktor
    def __init__(self, anz=2):
        self.anzSpieler = anz
        self.aktiveSpieler = anz

        self.spielergueltig[0] = True
        self.spielergueltig[1] = True
        if(anz > 2):
            self.spielergueltig[2] = True
            if(anz > 3):
                self.spielergueltig[3] = True
            else:
                self.spielergueltig[3] = False
        else:
            self.spielergueltig[2] = False
            self.spielergueltig[3] = False

        self.phase = 0
        self.spielerDran=-1
        self.verstaerkung=0
        self.provAuswahl=0
        self.runde=0
        self.start = True


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


    #gibt die noch vorhandenen Spieler aus
    def getAktiveSpieler(self):
        return self.aktiveSpieler


    #gibt den Namen der angegebenen Provinz zurueck
    def nameVon(self, anz=1):
        return self.knotennamen[anz]


    #gibt den Spieler zurueck, der gerade an der Reihe ist
    def spielerAnReihe(self):
        return self.spielerDran + 1


    #prueft, ob der angegebene Spieler noch ueber Provinzen verfuegt, wenn nein, scheidet er aus dem spiel aus
    #(durch spieler{nr} = False
    def pruefeSpielerInSpiel(self, nr=1):
        val = False
        for s in self.info:
            if(self.info[s][1] == nr):
                val = True
        print("spieler",nr,val)
        if(not val):
            self.aktiveSpieler -=1

        print("aktivespieler:",self.aktiveSpieler)

        if(nr == 1):
            self.spielergueltig[0] = val
        elif(nr == 2):
            self.spielergueltig[1] = val
        elif(nr == 3):
            self.spielergueltig[2] = val
        elif(nr == 4):
            self.spielergueltig[3] = val



    def pruefeLand(self):
        if(self.info[1][1] == self.spielerDran and self.info[2][1] == self.spielerDran and self.info[3][1] == self.spielerDran and self.info[4][1] == self.spielerDran and self.info[5][1] == self.spielerDran and self.info[12][1] == self.spielerDran):
            self.land[0][1] = self.spielerDran

        if(self.info[9][1] == self.spielerDran and self.info[10][1] == self.spielerDran and self.info[11][1] == self.spielerDran):
            self.land[1][1] = self.spielerDran

        if(self.info[6][1] == self.spielerDran and self.info[7][1] == self.spielerDran and self.info[8][1] == self.spielerDran):
            self.land[2][1] = self.spielerDran


    #gibt die moegliche Anzahl an Verstaerkungs-Einheiten des angegebenen Spielers zurueck
    def berechneVerstaerkung(self, spieler):
        self.pruefeLand()
        spieler = int(spieler) + 1
        print(spieler)
        provinbesitz=0
        for prov in self.info:
            if(self.info[prov][1] == spieler):
                provinbesitz+=1

        verst = round(provinbesitz)

        for l in self.land:
            if self.land[l][1] == spieler:
                verst += self.land[l][2]

        return verst


    #gibt die aktuelle Phase zurueck
    def getPhase(self):
        return (self.phasetext[self.phase], self.phase)


    #erhoehe die Anzahl der Einheiten der angegebenen Provinz um 1
    def verstaerkeProv(self, numr, anzahl=1):
        if(self.verstaerkung > 0):
            self.info[numr][0] += anzahl
            self.verstaerkung -= 1


    def getVerstaerkung(self):
        return self.verstaerkung


    #bewege 'anzahl' Einheiten von Provinz'von' nach Provinz'nach'
    def bewege(self,von,nach,anzahl=1):
        if(self.info[von][0] > anzahl):
            self.info[von][0] -= anzahl
            self.info[nach][0] += anzahl


    #TODO 'spieler' greift von Provinz 'von' mit 'anz' Einheiten Provinz 'nach' an
    def angreifen(self, von, nach, anzahl, spieler):
        if(self.info[von][0] > anzahl):
            self.info[von][0] -= anzahl
            alterbesitzer = self.info[nach][1]
            self.info[nach][1] = spieler
            self.info[nach][0] = anzahl
            self.pruefeSpielerInSpiel(alterbesitzer)   #pruefe ob spieler noch provinzen hat


    #TODO
    def verschieben(self, provnr):
        pass


    #TODO Ki platziert Einheiten
    def ki_platzieren(self):
        pass


    #TODO Ki greift Nacbarprovinz an
    def ki_angreifen(self):
        pass


    #TODO Ki bewegt Einheiten
    def ki_bewegen(self):
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
        if(self.runde > 2): #hier Anzahl der Start-Runden festlegen(in denen nur platziert wird)
            if(self.phase == 3):
                naechster = (self.spielerDran + 1) % self.anzSpieler
                while(not self.spielergueltig[naechster]):
                    naechster = (naechster + 1) % self.anzSpieler
                self.spielerDran = naechster
                self.phase = 1
                print("Spieler", self.spielerAnReihe(), "ist an der Reihe")
            else:
                self.phase = (self.phase + 1) % 4

            if(self.phase == 1):
                self.verstaerkung = self.berechneVerstaerkung(self.spielerDran)   #wird zu beginn einer runde aufgerufen, nachdem der/die gegner fertig ist/sind

            print(self.phase, self.phasetext[self.phase])
            self.provAuswahl=0
            return self.phase
        else:
            #nur platzieren moeglich(beim start)
            self.phase = 1
            self.spielerDran = (self.spielerDran + 1) % self.anzSpieler
            if(self.spielerDran == 0):
                self.runde += 1
            print(self.phase, self.phasetext[self.phase])
            self.provAuswahl = 0
            self.verstaerkung = self.berechneVerstaerkung(self.spielerDran)  # wird zu beginn einer runde aufgerufen, nachdem der/die gegner fertig ist/sind

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