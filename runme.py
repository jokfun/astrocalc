from tkinter import *
from tkinter.filedialog import *
from similarity import similarity
from agregate import agreg
from multiagregate import multiagreg
from helpApp import helpApp

win = Tk()
win.title("Application")

def cagreg(win):
    fen = agreg(win)
    fen.run()


def csimi(win):
    fen = similarity(win)
    fen.run()

def cmultiagreg(win):
    fen = multiagreg(win)
    fen.run()

def helpdoc(win):
    fen = helpApp(win)
    fen.run()
    
win.geometry("700x500")

menubar = Menu(win)


menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Similarity", command= lambda: csimi(win))
menu1.add_command(label="Agregate", command= lambda: cagreg(win))
menu1.add_command(label="MultiAgregate", command= lambda: cmultiagreg(win))
menubar.add_cascade(label="Application", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Help", command= lambda: helpdoc(win))
menubar.add_cascade(label="Other", menu=menu2)

win.config(menu=menubar)

#HelpDoc is launched by default
fen = helpApp(win)
fen.run()

win.mainloop()
