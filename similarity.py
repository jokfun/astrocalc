from tkinter import *
from tkinter.filedialog import *
from lecture import lecture
from relation import relation
from random import randint
import os


class similarity:

    def __init__(self,win):
        win.title("Similarity")
        self.fen1 = win
        listd = self.fen1.grid_slaves()
        for l in listd:
            l.destroy()
        self.source = None
        self.target = None


    def sourceFile(self):
        #Just select the csv files
        sourcef = askopenfilename(title="Select the source",
                                    initialdir=os.getcwd(),
                               filetypes=[('csv files','.csv')])
        try :
            self.source = open(sourcef,"r")
            self.nameT1 = sourcef
            self.txtfile1.configure(text = sourcef)
        except Exception as e:
            self.txtfile1.configure(text = "Erreur lors de l'ouverture du fichier")

    def targetFile(self):
        #Just select the csv files
        targetf = askopenfilename(title="Select the target",
                                    initialdir=os.getcwd(),
                               filetypes=[('csv files','.csv')])
        try :
            self.target = open(targetf,"r")
            self.nameT2 = targetf
            self.txtfile2.configure(text = targetf)
        except Exception as e:
            self.txtfile2.configure(text = "Erreur lors de l'ouverture du fichier")

    def addligne(self,tab, name):
        text = name + " :\n"
        
        for i in range(0,len(tab)):
            text += str(tab[i])+"\n"
        return text

    def savefile(self,savedata):
        """
            Seelct a save file
            Write the result in the save file selected
        """
        rep=os.getcwd()
        savemsg = ""
        nomfile = "save_"+str(randint(0,1000))
        try:
            repfic = asksaveasfilename(title="Save result",
                                                    initialdir=rep,
                                                    initialfile=nomfile,
                                                    filetypes = [("txt files",".txt")])
            if(len(repfic)>0):
                f = open(repfic+".txt","w")
                for k in savedata:
                    f.write(k)
                f.close()
                savemsg = "Results saved in : "+repfic+".txt"
            else:
                savemsg = "Change the save"
        except Exception as e:
            savemsg = 'Error while saving the file'
        self.errsave = Label(self.fen1, text =savemsg,justify="left")
        self.errsave.grid(row =8, column=3,sticky="w")

        
    def resum(self,tab):
        self.frame = Frame(self.fen1,width=400,height=300)
        self.frame.grid(row=6,column=3)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        
        ens = ["seed","percent","erreur"]
        text = ""
        for i in range(0,len(tab)):
            text+=self.addligne(tab[i],ens[i]) + "\n"
        self.res = Text(self.frame,borderwidth=3, relief="sunken",wrap='word')
        self.res.grid(row=0,column=0,padx=5,pady=5)
        self.res.insert(END, text)
        
        self.scrolly = Scrollbar(self.frame, command=self.res.yview)
        self.scrolly.grid(row=0, column=1, sticky='nsew')
        self.res['yscrollcommand'] = self.scrolly.set

        """
        scrollx = Scrollbar(frame, command=res.xview)
        scrollx.config(orient="horizontal")
        scrollx.grid(row=1, column=0, sticky='nsew')
        res['xscrollcommand'] = scrollx.set
        """

        return text

        

        
    def launch(self):
        if(self.source!=None and self.target!=None and type(self.source)!=list and type(self.target)!=list):

            seedget = self.seed.get()
            percentget = self.percent.get()

            try:
                fseed = int(seedget)
            except Exception:
                fseed = 100

            try:
                fpercent = int(percentget)
                if fpercent<=0 or fpercent>100:
                    fpercent = 100
            except Exception:
                fpercent = 100
            
            source,target = lecture(self.source,self.target,fseed,fpercent)
            result = relation(source,target)
            savetext = self.resum([[fseed], [fpercent]] + result)
            self.savef=Button(self.fen1, text="Save",command= lambda: self.savefile(savetext))
            self.savef.grid(row=7,column=3,sticky="W")
        else:
            self.txtfile3.configure(text = "Missing files")
     
    def run(self):

        #Select the Source
        self.txt1 = Label(self.fen1, text ='Source :')
        self.txt1.grid(row =1,column=1)

        self.txtfile1 = Label(self.fen1, text = "No file")
        self.txtfile1.grid(row =1, column=3,sticky=W)

        self.bouton1=Button(self.fen1, text="Select", command=self.sourceFile)
        self.bouton1.grid(row =1, column =2)


        #Select the target
        self.txt2 = Label(self.fen1, text ='Target :')
        self.txt2.grid(row =2, column=1)

        self.bouton2=Button(self.fen1, text="Select", command=self.targetFile)
        self.bouton2.grid(row =2, column =2)

        self.txtfile2 = Label(self.fen1, text = "No file") 
        self.txtfile2.grid(row =2, column=3,sticky=W)

        #Select the Seed
        self.txt3 = Label(self.fen1, text = 'Seed :')
        self.txt3.grid(row =3, column=1)

        self.seed = Entry(self.fen1, width=10)
        self.seed.grid(row =3, column=2)

        #Select the Percent
        self.txt4 = Label(self.fen1, text= 'Percent :')
        self.txt4.grid(row =4, column=1)

        self.percent = Entry(self.fen1, width=10)
        self.percent.grid(row =4, column=2)

        #Lauch
        self.lancement=Button(self.fen1, text="Launch",command=self.launch)
        self.lancement.grid(row=5, column=1)

        self.txtfile3 = Label(self.fen1, text = "Waiting to launch")
        self.txtfile3.grid(row =5, column=2)



     

