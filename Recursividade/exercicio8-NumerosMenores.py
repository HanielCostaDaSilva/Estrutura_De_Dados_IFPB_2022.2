def menores_rec(listaInt:list[int],key:int):
    valoresmenores=0
    if len(listaInt)==0:
        return 0
    if listaInt[0] <key:
        valoresmenores+=1
    valoresmenores+=menores_rec(listaInt[1:],key)
    return valoresmenores    

lista=[1,2,3,4,5,6,8,7,9,10,23,46,32,12,19,67]

chave=int(input('digite o valor que deseja conferir: '))

print('quantidade de valores menores: ',menores_rec(lista,chave))