from random import *
from tkinter import *

root = Tk()
theLabel = Label(root, text="Risiko")
theLabel.pack()
root.mainloop()


def wuerfeln(anz=1):
    assert anz >= 1, "falsche Anzahl an Wuerfeln"

    z = randint(1,6)
    while(anz > 1):
        z += randint(1, 6)
        anz -= 1
    return z

print("Starte wuerfel----------------------\n")
print("einmal wuerfeln =", wuerfeln())
print("zweimal wuerfeln =", wuerfeln(2))

