from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from intervalle import create_inter_with
from random import randint
from priority import createPriority
import functionAgreg as fagr
import os

def createAgreg(search,target,method,priority):
    """
        Make the agregation of each tuple between the source file and the target file
    """
    result = []
    for k in search:
        for i in range(0,len(target)):
            test = method(k[1],target[i][1],priority,tab=True)
            result.append([k[0],target[i][0],test])
    return result

class multiagreg:

    def __init__(self,win):
        win.title("MultiAgregate")
        self.fen1 = win
        
        #Clean the window
        listd = self.fen1.grid_slaves()
        for l in listd:
            l.destroy()
        self.source = None
        self.target = None
        self.method = None

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
            
    def selectsave(self):
        """
            Select the file where the result will be saved
        """
        rep=os.getcwd()
        nomfile = "save_"+str(randint(0,1000))
        self.repfic = asksaveasfilename(title="Save result",
                                        initialdir=rep,
                                        initialfile=nomfile,
                                        filetypes = [("txt files",".txt")])
        
    def savefile(self,savedata):
        """
            Write the result in the save file selected
        """
        savemsg = ""
        try:
            if(len(self.repfic)>0):
                f = open(self.repfic+".txt","w")
                for k in savedata:
                    f.write(k)
                f.close()
                savemsg = "Results saved in : "+self.repfic+".txt"
            else:
                savemsg = "Change the save"
        except Exception as e:
            savemsg = 'Error while saving the file'
        self.errsave = Label(self.fen1, text =savemsg,justify="left")
        self.errsave.grid(row =8, column=3,sticky="w")
        
    def resum(self,tab):
        """
            All the result of the algorithms are converted in a comprehensive language
        """
        text = "Source : "+self.nameT1+"\n"+"Target : "+self.nameT2+"\n\n"
        text += "Method used :"+str(self.method)+"\n"
        text += "Priority array : "+str(self.tabpriority)+"\n\n"
        for k in tab:
            text+=str(k[0][0])+","+str(k[1][0])+":"+str(k[2])+"\n"
        return text
        
        
    def launch(self):
        """
            Start the multiagregation
        """
        if(self.source!=None and self.target!=None and type(self.source)!=list and type(self.target)!=list):
            meth,name = fagr.function_agregation(self.method)
            self.method = name
            self.source_ = create_inter_with(self.source)
            self.target_ = create_inter_with(self.target)
            self.tabpriority = createPriority(self.priority.get())
            result = createAgreg(self.source_,self.target_,meth,self.tabpriority)
            savetext = self.resum(result)
            self.savefile(savetext)
            
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

        #Information for the distance
        self.txt3 = Label(self.fen1, text ='Distance :')
        self.txt3.grid(row =3, column=1)

        methdistance = fagr.name_agregation()
        methodName = StringVar()
        methodName.set(methdistance[0])
        self.listdistance = Combobox(self.fen1, textvariable = methodName,
                                values = methdistance, state="normal", width=15)
        self.listdistance.grid(row = 3, column=2)


        #Information of the priority
        self.txt4 = Label(self.fen1, text ='Priority :')
        self.txt4.grid(row =4, column=1)

        self.priorityDef = StringVar()
        self.priorityDef.set("1;1;1;1;1")
        self.priority = Entry(self.fen1, textvariable=self.priorityDef, width=20)
        self.priority.grid(row =4, column=2)
        
        #Save the result
        self.txt3 = Label(self.fen1, text ='Save file :')
        self.txt3.grid(row =5, column=1)
        
        self.save=Button(self.fen1, text="Select",command=self.selectsave)
        self.save.grid(row=5,column=2)
        
        #Launch the application
        self.lancement=Button(self.fen1, text="Launch",command= self.launch)
        self.lancement.grid(row=6, column=1)

        self.txtfile3 = Label(self.fen1, text = "Waiting to launch")
        self.txtfile3.grid(row =6, column=2)
