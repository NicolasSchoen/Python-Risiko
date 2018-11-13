import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter.messagebox import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import socket
import karte

class Risiko(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.title("Risiko")

        map = karte.Karte()

        self.frames = {}
        for F in (StartPage, Singleplayer, Multiplayer, Host, GuiMap, Join):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Risiko alpha 0.2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Nicolas Schön | Johannes Wimmer")
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Singleplayer",
                            command=lambda: controller.show_frame("Singleplayer"))
        button2 = tk.Button(self, text="Multiplayer",
                            command=lambda: controller.show_frame("Multiplayer"))
        button1.pack()
        button2.pack()


class Singleplayer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Singleplayer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main-Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        w = tk.Scale(self, from_=2, to=4, orient="horizontal")
        w.pack()

        button2 = tk.Button(self, text="Starte", command=lambda: controller.show_frame("GuiMap"))
        button2.pack()

    #def buttonStarte(self):
    #    map = karte.Karte(self.w.get())
    #    self.controller.show_frame("GuiMap")


class Multiplayer(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Multiplayer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Main-Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button2 = tk.Button(self, text="Join Game", command=lambda: controller.show_frame("Join"))
        button2.pack()

        button3 = tk.Button(self, text="Host Game", command=lambda: controller.show_frame("Host"))
        button3.pack()


class Host(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Multiplayer hosten", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="zurueck",
                           command=lambda: controller.show_frame("Multiplayer"))
        button.pack()

        stest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        stest.connect(("8.8.8.8", 80))

        labelip = tk.Label(self, text="IP-Adresse:" + stest.getsockname()[0])
        labelip.pack()
        label2 = tk.Label(self, text="Port")
        label2.pack()
        textbox = tk.Text(self, height=1, width=5)
        textbox.pack()


        button2 = tk.Button(self, text="Server starten",
                           command=lambda: showinfo("", "Starte Server mit IP " + stest.getsockname()[0] + " : " + textbox.get("1.0", 'end-1c')))
        button2.pack()


class Join(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Multiplayer beitreten", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="zurueck",
                           command=lambda: controller.show_frame("Multiplayer"))
        button.pack()
        label2 = tk.Label(self, text="IP-Adresse")
        label2.pack()
        textbox = tk.Text(self, height=1, width=15)
        textbox.pack()
        label3 = tk.Label(self, text="Port")
        label3.pack()
        textbox2 = tk.Text(self, height=1, width=5)
        textbox2.pack()


        button2 = tk.Button(self, text="Server beitreten",
                           command=lambda: showinfo("", "Server mit IP " + textbox.get("1.0", 'end-1c') + " : " + textbox2.get("1.0", 'end-1c') + " beitreten"))
        button2.pack()


#---------------------------------------------------Karte-GUI-----------------------------------------------------------
class GuiMap(tk.Frame):
    map = karte.Karte(4)
    map.felderInitialisieren()
    angriffvon = ""  # Hier wird Provinzid gespeichert, von der Angriff ausgeht
    aktiverSpieler = 1

    ##Start der Gui-initialisierung
    breite = 720
    hoehe = 720

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        button = tk.Button(self, text="Main-Menu",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



        #self = tk.Tk()
        #self = tk.Toplevel
        #theLabel = tk.Label(self, text="Risiko")
        #theLabel.pack()

        self.imganfang = tk.PhotoImage(file="..\\karte\\anfang.png")
        self.imgstart = tk.PhotoImage(file="..\\karte\\start.png")
        self.imgstart2 = tk.PhotoImage(file="..\\karte\\start2.png")
        self.imgstart3 = tk.PhotoImage(file="..\\karte\\start3.png")
        self.imgstart4 = tk.PhotoImage(file="..\\karte\\start4.png")
        self.imgverst = tk.PhotoImage(file="..\\karte\\verstaerkung.png")
        self.imgangriff = tk.PhotoImage(file="..\\karte\\angriff.png")
        self.imgbewegen = tk.PhotoImage(file="..\\karte\\bewegen.png")
        self.gif1 = tk.PhotoImage(file="..\\karte\\schiessen.gif")
        self.butt1 = tk.Button(self, image=self.imganfang, text="start", command=lambda: self.btn1func())

        self.butt1.pack()

        C = tk.Canvas(self, height=self.hoehe, width=self.breite)


        self.img = tk.PhotoImage(file="..\\karte\\map_small.png")
        C.create_image(0, 0, anchor= tk.NW, image=self.img)
        C.pack()

        # absolute platzierung der provinz-buttons
        #########################################################################################
        self.butt = [tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(),
                tk.Button(), tk.Button(), tk.Button()]
        # provinz1
        self.butt[1] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(1))
        self.butt[1].place(x=135, y=180)
        # provinz2
        self.butt[2] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(2))
        self.butt[2].place(x=70, y=220)
        # provinz3
        self.butt[3] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(3))
        self.butt[3].place(x=135, y=280)
        # provinz4
        self.butt[4] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(4))
        self.butt[4].place(x=120, y=350)
        # provinz5
        self.butt[5] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(5))
        self.butt[5].place(x=250, y=480)
        # provinz6
        self.butt[6] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(6))
        self.butt[6].place(x=450, y=250)
        # provinz7
        self.butt[7] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(7))
        self.butt[7].place(x=650, y=400)
        # provinz8
        self.butt[8] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(8))
        self.butt[8].place(x=500, y=405)
        # provinz9
        self.butt[9] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(9))
        self.butt[9].place(x=550, y=610)
        # provinz10
        self.butt[10] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(10))
        self.butt[10].place(x=400, y=650)
        # provinz11
        self.butt[11] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(11))
        self.butt[11].place(x=200, y=650)
        # provinz12
        self.butt[12] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(12))
        self.butt[12].place(x=220, y=150)

        #self.provinit()
        #self.mainloop()

    def btn1func(self):
        w = self.map.drueckeRunde()
        r = self.map.spielerAnReihe()
        self.provinit()

        # setze Farbe des Rundenbuttons
        if (r == 1):
            self.butt1.config(bg="lightblue")
        elif (r == 2):
            self.butt1.config(bg="yellow")
        elif (r == 3):
            self.butt1.config(bg="orange")
        elif (r == 4):
            self.butt1.config(bg="green")

        # waehle passendes Bild fuer Knopf
        if r != self.aktiverSpieler:
            if r == 1:
                self.butt1.config(image=self.imgstart)
            elif r == 2:
                self.butt1.config(image=self.imgstart2)
            elif r == 3:
                self.butt1.config(image=self.imgstart3)
            elif r == 4:
                self.butt1.config(image=self.imgstart4)
        elif w == 1:
            self.butt1.config(image=self.imgverst)
        elif w == 2:
            self.butt1.config(image=self.imgangriff)
        elif w == 3:
            self.butt1.config(image=self.imgbewegen)

    def btnprovfunc(self, zahl):
        self.provinit()

        rueckgabe = self.map.drueckeKnopf(zahl, self.aktiverSpieler)
        if (rueckgabe == None):

            print("Phase:", self.map.getPhase())

            if (self.map.getBesitzer(zahl) == self.aktiverSpieler):
                if (self.map.getPhase()[1] == 2):
                    self.nachbarnZeigen(1, zahl)
                elif (self.map.getPhase()[1] == 3):
                    self.nachbarnZeigen(2, zahl)
                elif (self.map.getPhase()[1] == 1):
                    self.provinit()
        elif (rueckgabe[0] == "angriff"):
            msg = "Schlacht von " + self.map.nameVon(zahl)
            print(msg)
            showinfo("Angriff", msg)
            self.provinit()
        elif (rueckgabe[0] == "bewegen"):
            self.provinit()

    def provinit(self):
        for x in range(13):
            if x != 0:
                self.butt[x].config(text=self.map.getProvInfo(x)[0])
                provinf = self.map.getProvInfo(x)
                if (provinf[1] == 1):
                    self.butt[x].config(bg="lightblue")
                elif (provinf[1] == 2):
                    self.butt[x].config(bg="yellow")
                elif (provinf[1] == 3):
                    self.butt[x].config(bg="orange")
                elif (provinf[1] == 4):
                    self.butt[x].config(bg="green")

    def nachbarnZeigen(self, modus, provid):  # modus = 1|2: angriff oder bewegen; privid = Provinz
        angriffvon = provid
        nbrn = self.map.nachbarn(provid)
        for x in range(len(nbrn)):
            if (modus == 1):
                if (self.map.getProvInfo(provid)[1] != self.map.getProvInfo(nbrn[x])[1]):
                    self.butt[nbrn[x]].config(bg="red")
            elif (modus == 2):
                if (self.map.getProvInfo(provid)[1] == self.map.getProvInfo(nbrn[x])[1]):
                    self.butt[nbrn[x]].config(bg="black")



if __name__ == "__main__":
    app = Risiko()
    app.mainloop()