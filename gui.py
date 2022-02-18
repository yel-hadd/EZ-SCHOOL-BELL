import tkinter as tk
from tkinter import ttk
from home import Home

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwarness(1)
except:
    pass

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('EZ SCHOOL BELL')
        self.geometry('661x551')
        self.frames = {}
        self.configure(bg = "#25414C")
        container = ttk.Frame(self)
        container.pack()
        self.show_frame(Home,None,None,None,None,None)

    def show_frame(self, container, a, b, c, d, e):
        if container == Home:
            Home(self).pack()

        """
        elif container == Contact:
            Contact(self).pack()
        elif container == Chapters:
            Chapters(self, a, b, c, d, e).pack()
        """


def btn_clicked():
    print('HI')

root = Window()
#root.iconbitmap("./app.ico")
root.resizable(False, False)
root.mainloop()
