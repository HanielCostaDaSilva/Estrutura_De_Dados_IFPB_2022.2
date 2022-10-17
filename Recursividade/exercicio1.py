def recursiveLength(string,tamanho=0)->int:
    if string=='':
        return tamanho
    #print(string[0], end=' ')
    elif string[0]==' ':
        tamanho=recursiveLength(string[1:],tamanho)
    else:
        tamanho= recursiveLength(string[1:],tamanho+1)

    return tamanho

palavra=input('string -> ')
print(recursiveLength(palavra))