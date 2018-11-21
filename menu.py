import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter.messagebox import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import socket
import os
import subprocess
#import multiplayer

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

        self.frames = {}
        for F in (StartPage, Singleplayer, Multiplayer, Host, Join):
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
    """Hauptmenue, Auswahl zwischen Singleplayer und Multiplayer"""

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


class Host(tk.Frame):
    """spiel erstellen, angabe des Ports"""

    def serverErstellen(self, port=""):
        if(port.isdigit() and (int(port) > 0 and int(port) < 65537)):
            showinfo("", "Starte Server mit IP " + self.stest.getsockname()[0] + " : " + port)
            #os.system("python risikoserver.py " + self.stest.getsockname()[0] + " " + port)
            #erzeuge extra prozess (damit hauptprogramm menu weiterlaeuft und nicht auf beendigung des servers wartet)
            subprocess.Popen(["python", "risikoserver.py", self.stest.getsockname()[0], port])
            #os.execv(os.curdir, ["python", "risikoserver.py", self.stest.getsockname()[0], port])
        else:
            showinfo("", "Bitte Port zwischen 1 und 65536 waehlen!")

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
        if (port.isdigit() and (int(port) > 0 and int(port) < 65537)):
            showinfo("", "Server mit IP " + ipadr + " : " + port + " beitreten")
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