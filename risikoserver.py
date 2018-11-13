from tkinter import *

"""Server-Anwendung"""
"""hier werden beigetretene Spieler und deren Status angezeigt"""



#beendet den Server
def servbeenden():
    #evtl. noch vorher sockets schliessen
    exit(0)

#startet den Server
def servstarten():
    pass

#fuege ki an stelle des spielers hinzu
def addKi():
    addKi.nr+=1
    if(addKi.nr < 5):
        spielername[addKi.nr-1] = "KI(" + str(addKi.nr) + ")"
    print(spielername)
    acttable()
addKi.nr=1

#aktualisiert tabelleneintraege
def acttable():
    spieler1.configure(text=spielername[0])
    status1.configure(text=status[0])
    spieler2.configure(text=spielername[1])
    status2.configure(text=status[1])
    spieler3.configure(text=spielername[2])
    status3.configure(text=status[2])
    spieler4.configure(text=spielername[3])
    status4.configure(text=status[3])


gui = Tk()
gui.title("Risiko Server 0.1")
#gui.configure(background="black")


#kopfzeile
kopf = Frame(gui)
Label(kopf, text="                        ").pack(side=LEFT)
Label(kopf, text="Risiko Server").pack(side=LEFT)
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
    spielername.append("spieler(" + str(x+1) + ")")
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
Button(tabl, text="+ KI", command=lambda: addKi()).pack()
tabl.pack(expand= True)

#Button Spiel starten
buttstart = Button(gui, text="Spiel starten", bg="lightgreen", command = lambda : servstarten())
buttstart.pack()



gui.mainloop()