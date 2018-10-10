from random import *


def wuerfeln(anz=1):
    assert anz >= 1, "falsche Anzahl an Wuerfeln"

    z = randint(1,6)
    while(anz > 1):
        z += randint(1, 6)
        anz -= 1
    return z