def insertionSort(arrayDesordenado:list):
    arrayOrdenado=[arrayDesordenado.pop(0)]
    
    for i in range(len(arrayDesordenado)):
        
        if arrayOrdenado[0] >= arrayDesordenado[0]: #se for menor que o primeiro índice, insere no começo
            arrayOrdenado.insert(0,arrayDesordenado.pop(0))
        
        else:# se for maior que o primeiro índice
            for j in range(len(arrayOrdenado)+1):
                if j == len(arrayOrdenado): #chegou no final da lista
                    arrayOrdenado.insert(j,arrayDesordenado.pop(0))#então insere no último elemento
                
                elif arrayOrdenado[j]>=arrayDesordenado[0]: #testa se o valor do array ordenado é maior que o que vai ser inserido
                    arrayOrdenado.insert(j,arrayDesordenado.pop(0)) #se o do Ordenado for maior, ele inserirá naquela posição
                    break
    return arrayOrdenado
                
array=[21,32,28,49,50,7,52,1,99,61,38,29,29,10,11,22,0,39]
print(array)
array= insertionSort( array )
print(array)