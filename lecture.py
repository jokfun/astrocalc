import sys
from intervalle import create_inter_without
from random import seed,shuffle

      
def lecture(source=None,target=None,fseed=100,fpercent=100):
    """
        Create conversion of the source file and the target file
        Shuffle method is used, base on the seed (default 100) 
    """
    seed(fseed)
    try:
        copysource = []
        copytarget = []
        if(source!=None and target!=None):
            source = create_inter_without(source)
            target = create_inter_without(target)
            shuffle(source)
            shuffle(target)

            for i in range(0,(int(len(source)*fpercent/100))):
                copysource.append(source[i])
            if(len(copysource)==0):
                copysource.append(source[0])
                
            for i in range(0,(int(len(target)*fpercent/100))):
                copytarget.append(target[i])
            if(len(copytarget)==0):
                copytarget.append(target[0])

        return copysource,copytarget
    except Exception as e:
        print(e)

    
