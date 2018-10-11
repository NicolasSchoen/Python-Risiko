class Karte:

    anzSpieler=2

    #phase: 0=warte auf spieler, 1=verstearkung, 2=angriff, 3=bewegen
    phasetext = ["gegner wartet", "Verstaerkungsphase", "Angriffsphase", "Bewegungsphase"]

    #12 Provinzen(möglich fuer 2, 3 und 4 spieler: 6, 4, 3)

    #"knoten" : (nachbar1, nachbar2)
    knotennamen = {1 : "thessalonike", 2 : "olymp", 3:"athen", 4:"sparta", 5:"kreta", 6:"anatolien", 7:"naher osten", 8:"zypern", 9:"sinai", 10:"aegypten", 11:"libyen", 12:"byzanz"}
    knotenzahl = {1 : [2,12], 2 : [1,3], 3 : [2,4], 4 : [2,3,5], 5 : [4,6], 6 : [5,7,8,12], 7 : [6,8,9], 8 : [6,7], 9 : [7,10], 10 : [9,11], 11 : [10], 12 : [1,6]}

    # "info" : (anzEinheiten, BesitzerId)
    info = {"provinz1" : (5,2), "provinz2" : (2,1)}


    def __init__(self, anz=2):
        anzSpieler = anz
        self.phase = 0
        self.spielerDran=0


    def nachbarn(self, knoten=1):
        return self.knotenzahl[knoten]#gibt tupel von knoten zurück


    def nameVon(self, anz=1):
        return self.knotennamen[anz]


    def drueckeKnopf(self, numr):
        #assert (isinstance(int, numr) and (numr<= 12 and numr > 0)), "Fehlerhafte Provinz gewaehlt"
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