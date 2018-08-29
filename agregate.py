from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from intervalle import create_inter_with
from random import randint
from priority import createPriority
import functionAgreg as fagr
import os


def addligne(tab,pos):
    """
        Transform an indice of the array result into a comprehensive one
    """
    result = "Test "+str(pos)+"\n"
    result+="Id of the test :"+str(tab[0][0][0])+"\n"
    result+="Details :\n"+str(tab[0][0][1:])+"\n"
    result+="Id of the best match :"+str(tab[1][0][0])+"\n"
    result+="Details :\n"+str(tab[1][0][1:])+"\n\n"
    return result

def searchsim(search,target,method,priority):
    """
        Find all the best match between a source and a target
    """
    result = []
    for k in search:
        best = method(k[1],target[0][1],priority)
        pos = 0
        #For one element in the source, we search his best match in the target
        for i in range(0,len(target)):
            test = method(k[1],target[i][1],priority)
            if(test<best):
                best = test
                pos = i
        result.append([k,target[pos]])
    return result
  

class agreg:

    def __init__(self,win):
        win.title("Agregate")
        self.fen1 = win
        
        #Cleaning the window
        listd = self.fen1.grid_slaves()
        for l in listd:
            l.destroy()
        self.source = None
        self.target = None
        self.method = None

    def sourceFile(self):
        """
            Create the source file
        """
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
        """
            Create the target file
        """
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


    def takemethod(self,event):
        """
            Update of the method with the ComboboxSelected
        """
        self.method = self.listdistance.get()

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
        """
            New frame is created to display the result of the algorithms (agregate)
        """
        self.frame = Frame(self.fen1,width=400,height=300)
        self.frame.grid(row=6,column=3)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        text = "Source : "+self.nameT1+"\n"+"Target : "+self.nameT2+"\n\n"
        text += "Method used :"+str(self.method)+"\n"
        text += "Priority array :"+str(self.tabpriority)+"\n\n"
        for i in range(0,len(tab)):
            text+=addligne(tab[i],i+1)
        self.res = Text(self.frame,borderwidth=3, relief="sunken",wrap='word')
        self.res.grid(row=0,column=0,padx=5,pady=5)
        self.res.insert(END, text)

        #Text can be too long, a scrollbar is used to reduce the size of the frame
        self.scrolly = Scrollbar(self.frame, command=self.res.yview)
        self.scrolly.grid(row=0, column=1, sticky='nsew')
        self.res['yscrollcommand'] = self.scrolly.set

        return text
        
        
    def launch(self):
        """
            Launch the algorithms
            Method will check if the input are corrects
        """
        #Checking if inputs are correct
        if(self.source!=None and self.target!=None and type(self.source)!=list and type(self.target)!=list):
            meth,name = fagr.function_agregation(self.method)
            self.method= name
            self.source_ = create_inter_with(self.source)
            self.target_ = create_inter_with(self.target)
            self.tabpriority = createPriority(self.priority.get())
            result = searchsim(self.source_,self.target_,meth,self.tabpriority)
            savetext = self.resum(result)
            
            self.savef=Button(self.fen1, text="Save",command= lambda: self.savefile(savetext))
            self.savef.grid(row=7,column=3,sticky="W")
            
        else:
            self.txtfile3.configure(text = "Missing files")

    def run(self):
        #Information for the source
        self.txt1 = Label(self.fen1, text ='Source :')
        self.txt1.grid(row =1,column=1)

        self.txtfile1 = Label(self.fen1, text = "No file")
        self.txtfile1.grid(row =1, column=3,sticky=W)
        

        self.bouton1=Button(self.fen1, text="Select", command=self.sourceFile)
        self.bouton1.grid(row =1, column =2)


        #Information for the target
        self.txt2 = Label(self.fen1, text ='Target :')
        self.txt2.grid(row =2, column=1)
        
        self.bouton2=Button(self.fen1, text="Select", command= self.targetFile)
        self.bouton2.grid(row =2, column =2)

        self.txtfile2 = Label(self.fen1, text = "No file")
        self.txtfile2.grid(row =2, column=3,sticky=W)

        #Information of the priority
        self.txt4 = Label(self.fen1, text ='Priority :')
        self.txt4.grid(row =3, column=1)

        self.priorityDef = StringVar()
        self.priorityDef.set("1;1;1;1;1")
        self.priority = Entry(self.fen1, textvariable=self.priorityDef, width=20)
        self.priority.grid(row =3, column=2)
        
        #Information for the distance
        self.txt3 = Label(self.fen1, text ='Distance :')
        self.txt3.grid(row =4, column=1)

        methdistance = fagr.name_agregation()
        methodName = StringVar()
        methodName.set(methdistance[0])
        self.listdistance = Combobox(self.fen1, textvariable = methodName,
                                values = methdistance, state="normal")
        self.listdistance.grid(row = 4, column=2)
        self.listdistance.bind("<<ComboboxSelected>>",self.takemethod)
        
        #Launch the application
        self.lancement=Button(self.fen1, text="Launch",command= self.launch)
        self.lancement.grid(row=5, column=1)

        self.txtfile3 = Label(self.fen1, text = "Waiting to launch")
        self.txtfile3.grid(row =5, column=2)
