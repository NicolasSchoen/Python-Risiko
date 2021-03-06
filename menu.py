import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter.messagebox import *
import socket
import subprocess
import sqlite3

class Risiko(tk.Tk):
    """Hauptklasse"""

    def __init__(self, *args, **kwargs):
        """erzeugt verschiedene frames und legt sie in stack ab, oberster frame wird angezeigt"""
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

        self.frames = {}
        for F in (StartPage, Singleplayer, Multiplayer, Highscore, Host, Join):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """zeigt den angegebenen frame an"""
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    """Hauptmenue, Auswahl zwischen Singleplayer und Multiplayer"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Risiko v1.0", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Nicolas Schön | Johannes Wimmer")
        label2.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Singleplayer",
                            command=lambda: controller.show_frame("Singleplayer"))
        button2 = tk.Button(self, text="Multiplayer",
                            command=lambda: controller.show_frame("Multiplayer"))
        button3 = tk.Button(self, text="Highscore", command=lambda: controller.show_frame("Highscore"))
        button1.pack()
        button2.pack()
        button3.pack()


class Singleplayer(tk.Frame):
    """Singleplayer-Auswahl, festlegen der anzahl KI-Gegner und starten des Spiels"""

    def starteSingleplayer(self, anzgegner=""):
        subprocess.Popen(["python", "singleplayer.py", anzgegner, "1"])

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Singleplayer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Hauptmenue",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        self.w = tk.Scale(self, from_=2, to=4, orient="horizontal")
        self.w.pack()

        button2 = tk.Button(self, text="Starte", command=lambda: self.starteSingleplayer(str(self.w.get())))
        button2.pack()

    #def buttonStarte(self):
    #    map = karte.Karte(self.w.get())
    #    self.controller.show_frame("GuiMap")


class Multiplayer(tk.Frame):
    """Multiplayer Auswahl, wahl zwischen beitreten und hosten"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Multiplayer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Hauptmenue",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        button2 = tk.Button(self, text="Spiel beitreten", command=lambda: controller.show_frame("Join"))
        button2.pack()

        button3 = tk.Button(self, text="Spiel erstellen", command=lambda: controller.show_frame("Host"))
        button3.pack()


class Highscore(tk.Frame):
    """Multiplayer Auswahl, wahl zwischen beitreten und hosten"""

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Highscore", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Hauptmenue",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

        btnauswahl = tk.Frame(self)
        button2 = tk.Button(btnauswahl, text="top10", command=lambda: self.showHighscore(True))
        button2.pack(side="left")
        button3 = tk.Button(btnauswahl, text="letzte10", command=lambda: self.showHighscore(False))
        button3.pack(side="left")
        btnauswahl.pack()

        self.hscore = tk.Label(self, text="")
        self.hscore.pack()


    def showHighscore(self, top10 = True):
        """zeigt entweder top 10 oder die letzten 10 eintraege"""
        if(top10):
            hs = "Top 10 Ergebnisse:\n"
        else:
            hs = "Letzte 10 Ergebnisse: \n"
        conn = sqlite3.connect('risiko.db')
        c = conn.cursor()
        #c.execute('''CREATE TABLE IF NOT EXISTS highscore
        #            (datum text, score int)''')

        rang=1
        if(top10):
            for row in c.execute("SELECT score FROM highscore ORDER BY highscore.score DESC limit 10"):
                print(row)
                if(rang <= 10):
                    hs += str(rang) + ": " + str(row[0]) + "\n"
                rang += 1
        else:
            for row in c.execute("SELECT score FROM highscore ORDER BY highscore.datum DESC limit 10"):
                print(row)
                if(rang <= 10):
                    hs += str(rang) + ": " + str(row[0]) + "\n"
                rang += 1

        conn.commit()
        conn.close()


        self.hscore.config(text=hs)


class Host(tk.Frame):
    """spiel erstellen, angabe des Ports"""

    def serverErstellen(self, port=""):
        """prueft port und startet server"""
        if(port.isdigit() and (int(port) > 0 and int(port) < 65536)):
            #showinfo("", "Starte Server mit IP " + self.stest.getsockname()[0] + " : " + port)
            #os.system("python risikoserver.py " + self.stest.getsockname()[0] + " " + port)
            #erzeuge extra prozess (damit hauptprogramm menu weiterlaeuft und nicht auf beendigung des servers wartet)
            subprocess.Popen(["python", "risikoserver.py", self.stest.getsockname()[0], port])
            #os.execv(os.curdir, ["python", "risikoserver.py", self.stest.getsockname()[0], port])
        else:
            showinfo("", "Bitte Port zwischen 1 und 65535 waehlen!")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Spiel erstellen", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="zurueck",
                           command=lambda: controller.show_frame("Multiplayer"))
        button.pack()

        self.stest = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.stest.connect(("8.8.8.8", 80))

        labelip = tk.Label(self, text="IP-Adresse:" + self.stest.getsockname()[0])
        labelip.pack()
        label2 = tk.Label(self, text="Port")
        label2.pack()
        self.textbox = tk.Text(self, height=1, width=5)
        self.textbox.pack()


        button2 = tk.Button(self, text="Server starten",
                           command=lambda: self.serverErstellen(self.textbox.get("1.0", 'end-1c')))
        button2.pack()


class Join(tk.Frame):
    """spiel beitreten, angabe der ip-adresse und des ports"""


    def spielBeitreten(self, ipadr="", port=""):
        """tritt spiel mit angegebener ip und port bei"""
        if (ipadr and port.isdigit() and (int(port) > 0 and int(port) < 65537)):
            #showinfo("", "Server mit IP " + ipadr + " : " + port + " beitreten")
            subprocess.Popen(["python", "multiplayer.py", str(ipadr), str(port)])
        else:
            showinfo("", "Bitte Port zwischen 1 und 65536 waehlen!")

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Spiel beitreten", font=controller.title_font)
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
                           command=lambda: self.spielBeitreten(textbox.get("1.0", 'end-1c'), textbox2.get("1.0",'end-1c')))
        button2.pack()



if __name__ == "__main__":
    app = Risiko()
    app.mainloop()