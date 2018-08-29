from math import fabs
import csv

def create_inter_without(file):
    """
        Convert the data of the file into all the intervals
    """
    try:
        result = []
        
        #With reset cursor, we can re-use input files.
        file.seek(0,0)
        modif = csv.reader(file)
        for k in modif:
            try:
                if(k[0]!="#"):
                    ligne = []
                    for i in range(2,7):
                        nbr1 = fabs(  round(float(k[i]),3)  )
                        nbr2 = fabs(  round(float(k[i+5]),3)  )
                        ligne.append([nbr1 - nbr2 , nbr1 + nbr2])
                    result.append(ligne)
            except Exception as e:
                print("Error :",k)
                print(e)
        return result
    except Exception as e:
        print (e)

def create_inter_with(file):
    """
        Convert the data of the file into all the intervals
        Assignments of the intervals are conserved
    """
    try:
        result = []

        #With reset cursor, we can re-use input files.
        file.seek(0,0)
        modif = csv.reader(file)
        for k in modif:
            try:
                if(k[0]!="#"):
                    ligne = []
                    for i in range(2,7):
                        nbr1 = fabs(  round(float(k[i]),3)  )
                        nbr2 = fabs(  round(float(k[i+5]),3)  )
                        ligne.append([nbr1 - nbr2 , nbr1 + nbr2])
                    result.append([k,ligne])
            except Exception as e:
                print("Error :",k)
                print(e)
        return result
    except Exception as e:
        print (e)
