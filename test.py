import unittest
import wuerfel
import karte
import random

class Test(unittest.TestCase):

    def test_wurf(self):
        self.assertTrue(1 <= wuerfel.wuerfeln() <= 6)

    def test_name1(self):
        map = karte.Karte()
        self.assertTrue(map.nameVon(1) == "thessalonike")

    def test_name2(self):
        map = karte.Karte()
        self.assertTrue(map.nameVon(7) == "naher osten")

    def test_namezufaellig(self):
        map = karte.Karte()
        self.assertTrue(map.nameVon(11) == "libyen")

    #Teste zufaellig eine Provinz auf nachbarn
    def test_nachbarn(self):
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(len(map.nachbarn(prov)) >= 1)

    def test_besitzer(self):
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(1 <= map.getBesitzer(prov) <= 4)

    def test_truppen(self):
        map = karte.Karte()
        prov = random.randint(1, 12)
        self.assertTrue(map.getTruppen(prov) >= 1)

    def test_aktiveSpieler(self):
        map = karte.Karte()
        self.assertTrue(4 >= map.getAktiveSpieler() >= 1)

    def test_gesamtEinheiten(self):
        map = karte.Karte()
        self.assertTrue(map.zaehleEinheiten() >= 12)

    def test_spielerAnReiheStart(self):
        map = karte.Karte()
        self.assertTrue(map.spielerAnReihe() == 0)

    def test_score(self):
        map=karte.Karte()
        self.assertIsInstance(map.calculateScore(), int)

    def test_spielerVerstaerkung(self):
        map=karte.Karte()
        self.assertTrue(map.berechneVerstaerkung(1) >= 1)

    def test_phase(self):
        map = karte.Karte()
        self.assertTrue(0 <= map.getPhase()[1] < 4)

if __name__ == '__main__':
    unittest.main()