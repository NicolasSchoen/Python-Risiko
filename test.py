import unittest
import wuerfel
import karte
import random

class Test(unittest.TestCase):

    def test_wurf(self):
        """Teste, ob wuerfel-wert gueltig ist"""
        self.assertTrue(1 <= wuerfel.wuerfeln() <= 6)

    def test_name1(self):
        """Teste, ob name zu provinz passt"""
        map = karte.Karte()
        self.assertTrue(map.nameVon(1) == "thessalonike")

    def test_name2(self):
        """Teste, ob name zu provinz passt"""
        map = karte.Karte()
        self.assertTrue(map.nameVon(7) == "naher osten")

    def test_name3(self):
        """Teste, ob name zu provinz passt"""
        map = karte.Karte()
        self.assertTrue(map.nameVon(11) == "libyen")

    #Teste zufaellig eine Provinz auf nachbarn
    def test_nachbarn(self):
        """Teste zufaellige Provinz auf Nachbarn, Provinz muss Nachbarn besitzen"""
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(len(map.nachbarn(prov)) >= 1)

    def test_besitzer(self):
        """Teste, ob Provinz gueltigen Besitzer hat"""
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(1 <= map.getBesitzer(prov) <= 4)

    def test_truppen(self):
        """Teste, ob Provinz mindestends eine einheit besitzt"""
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(map.getTruppen(prov) >= 1)

    def test_aktiveSpieler(self):
        """Teste, ob ein moeglicher spieler an reihe ist"""
        map = karte.Karte()
        self.assertTrue(4 >= map.getAktiveSpieler() >= 1)

    def test_gesamtEinheiten(self):
        """Teste, ob gesamt mindestens 12 einheiten vorhanden sind, also fuer jede provinz mind eine einheit"""
        map = karte.Karte()
        self.assertTrue(map.zaehleEinheiten() >= 12)

    def test_spielerAnReiheStart(self):
        """Teste, ob zu beginn kein spieler dran ist"""
        map = karte.Karte()
        self.assertTrue(map.spielerAnReihe() == 0)

    def test_score(self):
        """Teste, ob der berechnete Score einem ganzzahlwert entspricht"""
        map=karte.Karte()
        self.assertIsInstance(map.calculateScore(), int)

    def test_spielerVerstaerkung(self):
        """Teste, ob aktiver spieler verstaerkung bekommt"""
        map=karte.Karte()
        self.assertTrue(map.berechneVerstaerkung(1) >= 1)

    def test_phase(self):
        """Teste, ob Phase im gueltigen bereich ist"""
        map = karte.Karte()
        self.assertTrue(0 <= map.getPhase()[1] < 4)

if __name__ == '__main__':
    unittest.main()