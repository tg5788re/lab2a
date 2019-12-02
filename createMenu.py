#
def createMenu(optionLIst):
    tmp = " ";  ct = 0
    for opt in optionList:
        tmp += str(ct) +'.'+opt+'\n'
        ct +=1
    return tmp
    
