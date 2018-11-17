from tkinter import *
import sys

"""Server-Anwendung"""
"""hier werden beigetretene Spieler und deren Status angezeigt"""


def servbeenden():
    """beende den Server"""
    #evtl. noch vorher sockets schliessen
    exit(0)


def servstarten():
    """starte den Server"""

    pass


def addKi():
    """fuege ki an stelle des spielers hinzu"""


    if(addKi.nr < 4):
        addKi.nr += 1
        spielername[addKi.nr-1] = "KI(" + str(addKi.nr) + ")"
        status[addKi.nr-1] = "beigetreten"
    print(spielername)
    acttable()


addKi.nr=1


def delKi():
    """entferne KI"""
    if(addKi.nr > 1):
        spielername[addKi.nr-1] = "Spieler(" + str(addKi.nr) + ")"
        status[addKi.nr - 1] = "-"
        addKi.nr-=1
    acttable()




def acttable():
    """aktualisiere tabelleneintraege"""

    spieler1.configure(text=spielername[0])
    status1.configure(text=status[0])
    spieler2.configure(text=spielername[1])
    status2.configure(text=status[1])
    spieler3.configure(text=spielername[2])
    status3.configure(text=status[2])
    spieler4.configure(text=spielername[3])
    status4.configure(text=status[3])


if len(sys.argv) != 3:
    exit(1)

ipaddr = str(sys.argv[1])
port = str(sys.argv[2])


gui = Tk()
gui.title("Risiko Server 0.1")
#gui.configure(background="black")

#kopfzeile
kopf = Frame(gui)
Label(kopf, text="                        ").pack(side=LEFT)
labelipadr = Label(kopf, text=(ipaddr + ":" + port))
labelipadr.pack(side=LEFT)
#Button beenden
buttbeenden = Button(kopf, text="Server beenden", fg="white", bg="red" , command= lambda : servbeenden())
buttbeenden.pack(side=LEFT)

kopf.pack()

#Tabelle der Spieler
tabl = Frame(gui)
zeile = Frame(tabl)
zeile1 = Frame(tabl)
zeile2 = Frame(tabl)
zeile3 = Frame(tabl)
zeile4 = Frame(tabl)
spielername = []
status = []
#noch dummy werte
for x in range(4):
    spielername.append("Spieler(" + str(x+1) + ")")
    status.append("-")

Label(zeile, text="Spieler").pack(side=LEFT)
Label(zeile, text="Status").pack(side=LEFT)
zeile.pack()

spieler1 = Label(zeile1, text=spielername[0])
spieler1.pack(side = LEFT)
status1 = Label(zeile1, text=status[0])
status1.pack(side = LEFT)
zeile1.pack()

spieler2 = Label(zeile2, text=spielername[1])
spieler2.pack(side = LEFT)
status2 = Label(zeile2, text=status[1])
status2.pack(side = LEFT)
zeile2.pack()

spieler3 = Label(zeile3, text=spielername[2])
spieler3.pack(side = LEFT)
status3 = Label(zeile3, text=status[2])
status3.pack(side = LEFT)
zeile3.pack()

spieler4 = Label(zeile4, text=spielername[3])
spieler4.pack(side = LEFT)
status4 = Label(zeile4, text=status[3])
status4.pack(side = LEFT)
zeile4.pack()

print(spielername, status)
zeileki = Frame(tabl)
Button(zeileki, text="+ KI", command=lambda: addKi()).pack(side=LEFT)
Button(zeileki, text="- KI", command=lambda: delKi()).pack(side=LEFT)
zeileki.pack()
tabl.pack(expand= True)

#Button Spiel starten
buttstart = Button(gui, text="Spiel starten", bg="lightgreen", command = lambda : servstarten())
buttstart.pack()



gui.mainloop()