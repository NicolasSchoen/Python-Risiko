#Schlacht-Gui-Klasse
from tkinter import *
from tkinter.messagebox import *
import wuerfel


class Schlacht:



    def __init__(self, provname, eigene, gegner):
        self.provinzname = provname
        self.eigeneEinheiten = eigene
        self.gegnerEinheiten = gegner



