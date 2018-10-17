import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2
import kartegui

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
        for F in (StartPage, Singleplayer, Multiplayer, Join):
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

        button2 = tk.Button(self, text="Starte (1 Gegner)", command=lambda: kartegui.GuiKarte())
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

        button3 = tk.Button(self, text="Host Game", command=lambda: controller.show_frame("StartPage"))
        button3.pack()


class Join(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Singleplayer", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        label2 = tk.Label(self, text="Port")
        label2.pack()
        textbox = tk.Text(self, height=1, width=5)
        textbox.pack()
        button = tk.Button(self, text="zurueck",
                           command=lambda: controller.show_frame("Multiplayer"))
        button.pack()

        button2 = tk.Button(self, text="beitreten",
                           command=lambda: controller.show_frame("StartPage"))
        button2.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()