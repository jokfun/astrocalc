from math import fabs

def name_agregation():
    """
        Return all the method name
    """
    return (
        "Min Max",
        "Default"
        )

def function_agregation(meth):
    """
        Return a dictionnary of all the methods' name pointing on the methods
    """
    dic =  {
        "Min Max" : fminmax,
        "Default" : fminmax
        }
    try:
        return dic[meth],meth
    except Exception as e:
        return dic["Default"],"Min Max"
    

def fminmax(tab1,tab2,priority,tab=False):
    """
        Min Max function
        With 2 intervals [a;b] and [x;y] where a<=b and x<=y and a priority array
        result_i = (|a_i-x_i|+|b_i-y_i|)*priority[i]
        if you want a array result (MULTIAGREGATE) you will have :
            [result_1,result_2,result_3,result_4,result_5]
        else (AGREGATE) you will have :
            result_1 + result_2 + result_3 + result_4 + result_5
    """
    if(tab==False):
        score = 0
        for i in range(0,len(tab1)):
            score+= (fabs(  tab1[i][0] - tab2[i][0] ) + fabs( tab1[i][1] - tab2[i][1] ) )  * priority[i]
        return score
    else:
        tab = []
        for i in range(0,len(tab1)):
            score= (fabs(  tab1[i][0] - tab2[i][0] ) + fabs( tab1[i][1] - tab2[i][1] ) )  * priority[i]
            tab.append(round(score,4))
        return tab
