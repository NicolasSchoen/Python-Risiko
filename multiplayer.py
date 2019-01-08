from random import *
from tkinter import *
from tkinter.messagebox import *
import sys
import time
import threading
import sqlite3
import socket


#---------------------------------------------------Singleplayer-GUI-----------------------------------------------------------
"""Gui hat keinen Zugriff auf Karte-Klasse"""


def btn1func():
    """Rundenbutton"""
    global istDran
    global semaphorBtn

    if(istDran):
        semaphorBtn = False
        clientSocket.send("rundenButton".encode())
        leseAntwort()

def btnprovfunc(zahl):
    """Provinzbutton"""
    global istDran
    global semaphorBtn
    global provinf
    global aktiverSpieler

    if(istDran):
        if(provinf[zahl][1] == aktiverSpieler):
            slider.config(to=provinf[zahl][0] - 1)
        msg = "provButton:" + str(zahl) + ":" + str(slider.get())
        semaphorBtn = False
        clientSocket.send(msg.encode())
        leseAntwort()


def provinit():
    """initialisiere farbe und text der provinzbuttons"""
    global provinf
    global spielerDran
    global phase
    global verstaerkung
    global istDran
    global aktiverSpieler

    print("initialize province")
    print(provinf)
    for x in range(13):
        if x != 0:
            #provinf = [0,0]                                                             #!Dummy
            if (provinf[x][1] == 1):
                butt[x].config(bg="lightblue", text=str(provinf[x][0]))
            elif (provinf[x][1] == 2):
                butt[x].config(bg="yellow", text=str(provinf[x][0]))
            elif (provinf[x][1] == 3):
                butt[x].config(bg="orange", text=str(provinf[x][0]))
            elif (provinf[x][1] == 4):
                butt[x].config(bg="green", text=str(provinf[x][0]))
        else:
            spielerDran = int(provinf[0][1])
            phase = int(provinf[0][2])
            verstaerkung = int(provinf[0][3])
            if(spielerDran == aktiverSpieler):
                istDran = True
            else:
                istDran = False

            rundenbuttonInit()


def rundenbuttonInit():
    """initialisiere farbe und bild des rundenbuttons"""
    global spielerDran
    global phase
    global istDran
    global verstaerkung
    # setze Farbe des Rundenbuttons
    if (spielerDran == 1):
        butt1.config(bg="lightblue")
    elif (spielerDran == 2):
        butt1.config(bg="yellow")
    elif (spielerDran == 3):
        butt1.config(bg="orange")
    elif (spielerDran == 4):
        butt1.config(bg="green")

    # waehle passendes Bild fuer Knopf
    if(not istDran):
        if spielerDran == 1:
            butt1.config(image=imgstart)
        elif spielerDran == 2:
            butt1.config(image=imgstart2)
        elif spielerDran == 3:
            butt1.config(image=imgstart3)
        elif spielerDran == 4:
            butt1.config(image=imgstart4)
    elif phase == 1:
        butt1.config(image=imgverst)
        labeltext.config(text="noch " + str(verstaerkung) + " Einheiten platzieren")
    elif phase == 2:
        labeltext.config(text="Angriff mit #Einheiten")
        butt1.config(image=imgangriff)
    elif phase == 3:
        labeltext.config(text="Bewegen von #Einheiten")
        butt1.config(image=imgbewegen)

def nachbarnZeigen(modus, provid):  # modus = 1|2: angriff oder bewegen; privid = Provinz
    pass


def idleplayer():
    """thread des spieler, laeuft im hintergrund, ermoeglicht druecken der buttons"""
    global istDran
    global semaphorBtn

    while True:
        if(semaphorBtn):
            time.sleep(0.5)
            clientSocket.send("info".encode())
            if(leseAntwort() == -1):
                break
    exit(0)


def leseAntwort():
    """liest antwort des Servers und entscheidet was zu tun ist"""
    global semaphorBtn

    antwort = clientSocket.recv(1024).decode()
    print("CLIENT:::::antwort=", antwort)
    if (antwort == 'exit'):
        print("Beende")
        istDran = False
        showinfo("", "Server wurde beendet, du kannst nun das Spiel schliessen!")
        return -1
    if (antwort[0] == '1'):  # Server sendet karteninfo
        print("zeige Karte an")
        decodeMap(antwort)
        provinit()
    if (antwort[0] == 'f'):
        spielAuswerten(antwort)
    semaphorBtn = True


def decodeMap(mapstr=""):
    """wandelt karte in textform(string) in liste der karteninformationen um"""
    # "info" : (anzEinheiten, BesitzerId)
    global provinf
    provinf = []

    prov = mapstr.split(":")
    provs = []
    for p in prov:
        provs.append(p.split(","))

    for p in provs:
        p[0] = int(p[0])
        p[1] = int(p[1])
        provinf.append(p)


def spielAuswerten(msg=""):
    """wertet ergebnis aus, bei gewinn wird score in DB geschrieben"""
    global aktiverSpieler
    feld = msg.split(":")
    if(int(feld[1]) == aktiverSpieler):
        gwtext = "Du hast gewonnen! Highscore=" + str(feld[2])
        showinfo("Gewonnen",gwtext)
        schreibeHighscore(int(feld[2]))
    else:
        showinfo("Verloren","Du hast verloren!")


def schreibeHighscore(score):
    """Highscore in Datenbank speichern"""
    conn = sqlite3.connect('risiko.db')
    c = conn.cursor()
    commnd = "INSERT INTO highscore VALUES ('" + str(time.time()) + "','" + str(score) + "')"
    c.execute(commnd)
    conn.commit()
    conn.close()
    print("Highscore erfolgreich in Datenbank gespeichert!")


if __name__ == '__main__':

    aktiverSpieler = 0  # vom server zugewiesen
    spielerDran = 0  # vom server zugewiesen
    phase = 0  # vom server zugewiesen
    verstaerkung = 0  # vom server zugewiesen
    letzteTruppen = 0
    istDran = False
    semaphorBtn = True
    if (len(sys.argv) != 3):
        showerror("Fehler", "nicht 2 Argumente angegeben!")
        exit(1)
    ipaddr = sys.argv[1]
    angriffvon = ""  # Hier wird Provinzid gespeichert, von der Angriff ausgeht
    port = int(sys.argv[2])


    provinf = [[0,0]]

    ##Start der Gui-initialisierung
    breite = 720
    hoehe = 720

    root = Tk()

    kopf = Frame(root)
    labeltext = Label(kopf, text=" ")
    labeltext.pack(side=LEFT)
    slider = Scale(kopf, from_=1, to=1, orient="horizontal")
    slider.pack(side=LEFT)
    kopf.pack()

    imganfang = PhotoImage(file="karte\\anfang.png")
    imgstart = PhotoImage(file="karte\\start.png")
    imgstart2 = PhotoImage(file="karte\\start2.png")
    imgstart3 = PhotoImage(file="karte\\start3.png")
    imgstart4 = PhotoImage(file="karte\\start4.png")
    imgverst = PhotoImage(file="karte\\verstaerkung.png")
    imgangriff = PhotoImage(file="karte\\angriff.png")
    imgbewegen = PhotoImage(file="karte\\bewegen.png")
    gif1 = PhotoImage(file="karte\\schiessen.gif")
    butt1 = Button(root, image=imganfang, text="start", command=lambda: btn1func())
    butt1.pack()

    C = Canvas(root, height=hoehe, width=breite)


    img = PhotoImage(file="karte\\map_small.png")
    C.create_image(0, 0, anchor=NW, image=img)
    C.pack()

    yoffset = 20
    # absolute platzierung der provinz-buttons
    #########################################################################################
    butt = [Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(), Button(),
            Button(), Button(), Button()]
    # provinz1
    butt[1] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(1))
    butt[1].place(x=135, y=180+yoffset)
    # provinz2
    butt[2] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(2))
    butt[2].place(x=70, y=220+yoffset)
    # provinz3
    butt[3] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(3))
    butt[3].place(x=135, y=280+yoffset)
    # provinz4
    butt[4] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(4))
    butt[4].place(x=120, y=350+yoffset)
    # provinz5
    butt[5] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(5))
    butt[5].place(x=250, y=480+yoffset)
    # provinz6
    butt[6] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(6))
    butt[6].place(x=450, y=250+yoffset)
    # provinz7
    butt[7] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(7))
    butt[7].place(x=650, y=400+yoffset)
    # provinz8
    butt[8] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(8))
    butt[8].place(x=500, y=405+yoffset)
    # provinz9
    butt[9] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(9))
    butt[9].place(x=550, y=610+yoffset)
    # provinz10
    butt[10] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(10))
    butt[10].place(x=400, y=650+yoffset)
    # provinz11
    butt[11] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(11))
    butt[11].place(x=200, y=650+yoffset)
    # provinz12
    butt[12] = Button(root, bg="grey", text="1", command=lambda: btnprovfunc(12))
    butt[12].place(x=220, y=150+yoffset)

    #provinit()

    #Server beitreten
    clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        clientSocket.connect((ipaddr,port))
    except socket.gaierror:
        showerror("Fehler", "Server offline oder Adresse falsch!")
        exit(3)
    except ConnectionRefusedError:
        showerror("Fehler", "falscher Port oder Server offline!")
    nachricht = "liketojoin"
    clientSocket.send(nachricht.encode())
    antwort = clientSocket.recv(1024).decode()
    if(len(antwort) == 4 and antwort[0] == 'o' and antwort[1] == 'k'):
        aktiverSpieler = int(antwort[3])
        print("SPIELER =",aktiverSpieler)
        root.title("Risiko Multiplayer, als Spieler " + str(aktiverSpieler) + " beigetreten")
        threading._start_new_thread(idleplayer,())
    else:
        showerror("Fehler", "Server voll!")
        exit(2)

    root.mainloop()