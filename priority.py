def createPriority(tab):
    """
        Convert the input priority into an array
        Default : [1,1,1,1,1]
    """
    try:
        tab = tab.replace(",",".")
        if(" " in tab and ";" in tab):
            tab = tab.replace(" ",";")
        if(";" in tab):
            tab = tab.split(";")
        else:
            tab = tab.split(" ")
        result = []
        for i in range(0,5):
            try:
                result.append(float(tab[i]))
            except:
                result.append(1.0)
        if len(result)<5:
            while(len(result)<5):
                result.append(1)
        return result
    except Exception as e:
        return [1,1,1,1,1]
