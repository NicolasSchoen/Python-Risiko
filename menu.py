import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import socket
import karte

class SampleApp(tk.Tk):

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
        label = tk.Label(self, text="Risiko v0.1", font=controller.title_font)
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

        button2 = tk.Button(self, text="Starte (1 Gegner)", command=lambda: controller.show_frame("GuiMap"))
        button2.pack()


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
                           command=lambda: controller.show_frame("StartPage"))
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
                           command=lambda: controller.show_frame("StartPage"))
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
        label = tk.Label(self, text="Risiko v0.2")
        label.pack(side="top", fill="x", pady=10)



        #self = tk.Tk()
        #self = tk.Toplevel
        #theLabel = tk.Label(self, text="Risiko")
        #theLabel.pack()

        imganfang = tk.PhotoImage(file="..\\karte\\anfang.png")
        imgstart = tk.PhotoImage(file="..\\karte\\start.png")
        imgstart2 = tk.PhotoImage(file="..\\karte\\start2.png")
        imgstart3 = tk.PhotoImage(file="..\\karte\\start3.png")
        imgstart4 = tk.PhotoImage(file="..\\karte\\start4.png")
        imgverst = tk.PhotoImage(file="..\\karte\\verstaerkung.png")
        imgangriff = tk.PhotoImage(file="..\\karte\\angriff.png")
        imgbewegen = tk.PhotoImage(file="..\\karte\\bewegen.png")
        gif1 = tk.PhotoImage(file="..\\karte\\schiessen.gif")
        butt1 = tk.Button(self, image=imganfang, text="start", command=lambda: self.btn1func())

        butt1.pack()

        C = tk.Canvas(self, height=self.hoehe, width=self.breite)


        img = tk.PhotoImage(file="..\\karte\\map_small.png")
        C.create_image(0, 0, anchor= tk.NW, image=img)
        C.pack()

        # absolute platzierung der provinz-buttons
        #########################################################################################
        butt = [tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(), tk.Button(),
                tk.Button(), tk.Button(), tk.Button()]
        # provinz1
        butt[1] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(1))
        butt[1].place(x=135, y=180)
        # provinz2
        butt[2] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(2))
        butt[2].place(x=70, y=220)
        # provinz3
        butt[3] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(3))
        butt[3].place(x=135, y=280)
        # provinz4
        butt[4] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(4))
        butt[4].place(x=120, y=350)
        # provinz5
        butt[5] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(5))
        butt[5].place(x=250, y=480)
        # provinz6
        butt[6] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(6))
        butt[6].place(x=450, y=250)
        # provinz7
        butt[7] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(7))
        butt[7].place(x=650, y=400)
        # provinz8
        butt[8] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(8))
        butt[8].place(x=500, y=405)
        # provinz9
        butt[9] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(9))
        butt[9].place(x=550, y=610)
        # provinz10
        butt[10] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(10))
        butt[10].place(x=400, y=650)
        # provinz11
        butt[11] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(11))
        butt[11].place(x=200, y=650)
        # provinz12
        butt[12] = tk.Button(self, bg="blue", text="1", command=lambda: self.btnprovfunc(12))
        butt[12].place(x=220, y=150)

        #self.provinit()
        #self.mainloop()

    def btn1func(self):
        w = map.drueckeRunde()
        r = map.spielerAnReihe()
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

        rueckgabe = map.drueckeKnopf(zahl, self.aktiverSpieler)
        if (rueckgabe == None):

            print("Phase:", map.getPhase())

            if (map.getBesitzer(zahl) == self.aktiverSpieler):
                if (map.getPhase()[1] == 2):
                    self.nachbarnZeigen(1, zahl)
                elif (map.getPhase()[1] == 3):
                    self.nachbarnZeigen(2, zahl)
                elif (map.getPhase()[1] == 1):
                    self.provinit()
        elif (rueckgabe[0] == "angriff"):
            msg = "Schlacht von " + map.nameVon(zahl)
            print(msg)
            tk.showinfo("Angriff", msg)
            self.provinit()
        elif (rueckgabe[0] == "bewegen"):
            self.provinit()

    def provinit(self):
        for x in range(13):
            if x != 0:
                self.butt[x].config(text=map.getProvInfo(x)[0])
                provinf = map.getProvInfo(x)
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
        nbrn = map.nachbarn(provid)
        for x in range(len(nbrn)):
            if (modus == 1):
                if (map.getProvInfo(provid)[1] != map.getProvInfo(nbrn[x])[1]):
                    self.butt[nbrn[x]].config(bg="red")
            elif (modus == 2):
                if (map.getProvInfo(provid)[1] == map.getProvInfo(nbrn[x])[1]):
                    self.butt[nbrn[x]].config(bg="black")



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()