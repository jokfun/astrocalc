from tkinter import *
class helpApp:
    
    def __init__(self,win):
        win.title("Application")
        self.fen1 = win
        
        #Cleaning the window
        listd = self.fen1.grid_slaves()
        for l in listd:
            l.destroy()

    def run(self):
        """
            In a new frame which used a Scrollbar
            Display all the informations of the docApp file
        """
        txt = ""
        try:
            file = open("docApp.txt","r")
            for k in file:
                txt+=k
            file.close()
        except Exception as e:
            txt = "Error while loading docApp.txt"
        
        self.frame = Frame(self.fen1,width=620,height=450)
        self.frame.grid(row=1,column=1)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.res = Text(self.frame,borderwidth=3, relief="sunken",wrap='word')
        self.res.grid(row=0,column=0,padx=5,pady=5)
        self.res.insert(END, txt)
        
        self.scrolly = Scrollbar(self.frame, command=self.res.yview)
        self.scrolly.grid(row=0, column=1, sticky='nsew')
        self.res['yscrollcommand'] = self.scrolly.set
