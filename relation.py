from time import time
#import hungarian as hg

def intervalle(result,tab,dic):
    """
        Group all element in an array, with 0 duplication by using a dictionary which works here as a memory
    """
    for ligne in tab:
        for ele in ligne:
            """
                All the trick is here
                By using a dic, we don't have to check all the elements in the array result
                It'll reduce the time process because size of array result will be bigger and bigger
            """
            try:
                a = dic[str(ele)]
            except Exception as e:
                dic[str(ele)] = []
                result.append(ele)
    return result,dic

def create_all(source,target):
    """
        Group all the element of the source and the target in a single array, with 0 duplication
        All existing interval of both files will be return
    """
    t = time()
    result = []
    dic = {}
    result,dic = intervalle(result,target,dic)
    result,dic = intervalle(result,source,dic)
    return result

def belongTo(interval,tab,name):
    """
        Build the condensed representation for interval-based relations 
    """
    result = []
    for i in range(0,len(interval)):
        for j in range(0,len(tab[0])):
            for k in range(0,len(tab)):
                if interval[i][0][0] >= tab[k][j][0] and interval[i][0][1] <= tab[k][j][1]:
                    interval[i].append(name+str(j))
                    break
                
    

def createError(inter,len1,len2,nsource,ntarget):
    """
        Build the error measures
    """
    result = []
    for i in range(0,len1):
        ligne = []
        for j in range(0,len2):
            valmax = 0
            valoccur = 0
            for k in inter:
                if nsource+str(i) in k:
                    valmax+=1
                if ntarget+str(j) in k and nsource+str(i) in k:
                    valoccur+=1
            ligne.append(1-(valoccur/valmax))
        result.append(ligne)
    return result

        
def relation(source,target):
    """
        Create the similarity between the source and the target
    """
    resum = []
    inter = create_all(source,target)
    new = []
    for k in inter:
        new.append([k])
    inter = new
    t = time()
    nameSource = "src"
    nameTarget = "trg"
    belongTo(inter,source,nameSource)
    belongTo(inter,target,nameTarget)
    taberror = createError(inter,len(source[0]),len(target[0]),nameSource,nameTarget)
    resum.append(taberror)

    
    """
    #Remove comment to test the example
    for k in taberror:
        print(k)
    """
    
    
    """
        Can return the hungarian result
    """
    
    #hungarian = hg.Hungarian(taberror)
    #hungarian.calculate()
    #result = hungarian.get_results()
    
    return resum

    

if __name__=="__main__":
    """
        Test to check if the algorithms used (SIMILARITY) are correct
    """
    source = [
        [[0,0.5],[0,1],[0,1]],
        [[1,1.5],[1,2],[3,3.5]],
        [[2,3],[1.5,4],[2,3]]
        ]
    target = [
        [[0,1.5],[1,2],[1.6,1.8],[2,3]],
        [[0,1.5],[1,2],[3.1,4],[2,3]],
        [[0,1.5],[0,1],[0,0.5],[1,2]],
        [[2,3.5],[2,3],[0,0.5],[1,2]],        
        [[2,3.5],[1,2],[0,0.5],[1,2]]
        ]
    relation(source,target)
