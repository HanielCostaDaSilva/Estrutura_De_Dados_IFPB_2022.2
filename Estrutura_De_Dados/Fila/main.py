#from filaSequencialCircular import *
from filaEncadeadaNoCabeca import *

#== == == == Variáveis
separador= '\n'+('-0-0'*30)

stringsLista=['Letra','UmaLetra','OutraLetra','TerceiraLetra','QuartaLetra','23']
inteirosLista=[0,2,4,6,8,10,12,14,16,18,20,22,24,26]

#== == == == Criando as filas
filaInteiros = Fila()
filaLetras=Fila()

#== == == == == Inserindo as filas

for i in stringsLista:
    filaLetras.enfileira(i)

for i in inteirosLista:
    filaInteiros.enfileira(i)

try:
    print(filaInteiros)
    print(filaLetras)
    print(separador)
    
    input(' ')
#== == == == == Buscando Elementos por posição   
    #print(filaLetras.busca('EstaLetra'))
    #print(filaInteiros.busca(13))
    print('buscando a posição de determinados nós')
    print(filaLetras.busca('UmaLetra'))
    print(filaInteiros.busca(6))
    print(separador)
    
    input(' ')
#== == == == ==Desenfileirando    
    print('Saiu este nó: ',filaInteiros.desenfileira())
    print('Saiu este nó: ',filaLetras.desenfileira())
    print(filaInteiros,'\n', filaLetras)
    print(separador)
    
    input(' ')
    #print(filaInteiros.elemento(20))
    #print(filaLetras.elemento(30))
    
#== == == == Descubrindo o conteudo de elementos através da posição 
    print('descobrindo o contéudo de uma posição X \n',filaInteiros.elemento(3))
    print(filaLetras.elemento(5))
    print(separador)
    
    input(' ')

#== == == == Modificando o conteudo de elementos 
    for i in range(3):
        filaInteiros.modificar(i+1,filaInteiros.elemento(i+1) *4)
    

    
    for j in range(3):
        filaLetras.modificar(j+1,'Não é ' + filaLetras.elemento(j+1))
    
    print('Modifcano os nós\n',filaInteiros,'\n\n', filaLetras)
    print(separador)
    input(' ')

#== == == == Esvaziando a Lista

    print('esvaziando a fila \n',filaLetras.esvazia())
    print(filaInteiros.esvazia())
    #print('\n',filaInteiros,'\n\n', filaLetras)
    print(separador)
    input(' ')


#== == == == Inserido elementos depois de apagar a lista:
    print('inserindo elementos em um nó depois de tê-lo esvaziado')
    for i in range(10):
        filaInteiros.enfileira((( (i+10) * 4 +2 ) %5)-12 )
        filaLetras.enfileira('Letra '* ( ((i+1)%3)+1) )
    print(filaInteiros)
    print(filaLetras)
    print(separador)
    input(' ')
    
#== == == == Possíveis excessões    
except FilaException as FE:
    print(FE)