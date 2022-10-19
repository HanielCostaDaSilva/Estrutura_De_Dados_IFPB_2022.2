def printstr(string):
    if string!='':
        print(string[0],end='\n')
        printstr(string[1:])
        
printstr('olá?     ')