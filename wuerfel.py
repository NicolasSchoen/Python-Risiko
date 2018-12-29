from random import *


def wuerfeln(anz=1):
    """wuerfelt mit 'anz' Wuerfeln und liefert das Erbgebnis als Rueckgabewert
    :param anz: Anzahl der Wuerfel
    :return: Ergebnis des Wurfs
    """
    assert anz >= 1, "falsche Anzahl an Wuerfeln"

    z = randint(1,6)
    while(anz > 1):
        z += randint(1, 6)
        anz -= 1
    return z