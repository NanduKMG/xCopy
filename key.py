from Tkinter import *
import sys
import Tkinter

class App(Tkinter.Tk):

    def __init__(self):
        Tkinter.Tk.__init__(self)
        menubar = Tkinter.Menu(self)
        fileMenu = Tkinter.Menu(menubar, tearoff=False)
        menubar.add_cascade(label="Copying", underline=0, menu=fileMenu)
        fileMenu.add_command(label="doThat", underline=1,
                             command=quit, accelerator="Ctrl+q")
        fileMenu.add_command(label="doThis", underline=1,
                             command=quit, accelerator="Ctrl+w")
        self.config(menu=menubar)

        self.bind_all("<Control-v>", self.doThat)
        self.bind_all("<Tab>", self.doThis)

    def doThat(self, event):
        print("Control q is pressed ...")

    def doThis(self, event):
        print("Control w is pressed...")

if __name__ == "__main__":
    app = App()
    app.mainloop()

