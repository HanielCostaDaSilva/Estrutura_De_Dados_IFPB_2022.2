def decToBin(inteiro:int)->int:
    if inteiro==0 or inteiro==1:
        return str(inteiro)
    
    restoDivisao=str(inteiro%2)
    binario= str(decToBin(inteiro//2)) +restoDivisao
    
    return int(binario)

inteiro=int(input('Digite o número que desejas transformar em binário: '))
print(f'o número: {inteiro} é na base binária: {decToBin(inteiro)}')

