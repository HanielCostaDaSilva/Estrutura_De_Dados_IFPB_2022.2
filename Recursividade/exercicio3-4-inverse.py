def invertString(string):
    if len(string)==0:
        return string
    return (invertString(string[1:])+ string[0])
    
def printInverse(string):
    if len(string)==0:
        print(string, end=' ')
    else:
        printInverse(string[1:])
        print(string[0], end=' ')
        
    

palavra='Eu estive aqui?'
print('========String invertida======== ')
print(invertString(palavra))
print('========Print invertido======== ')
palavra='Sim. Você esteve aqui'
printInverse(palavra)