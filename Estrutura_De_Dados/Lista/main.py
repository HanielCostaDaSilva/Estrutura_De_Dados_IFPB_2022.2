from listaSequencial import *
#from listaEncadeadaNoCabeca import *

#== == == == Variáveis
separador= '\n'+('-0-0'*30)

stringsLista=['Letra','UmaLetra','OutraLetra','TerceiraLetra','QuartaLetra','23']
inteirosLista=[0,2,4,6,8,10,12,14,16,18,20,22,24,26]

#== == == == Criando as listas
listaInteiros = Lista()
listaLetras=Lista()

#== == == == == Inserindo as listas

for i in stringsLista:
    listaLetras.inserir(0,i)

for i in inteirosLista:
    listaInteiros.inserir(0,i)

try:
    print(listaInteiros)
    print(listaLetras)
    print(separador)
    
    input(' ')
#== == == == == Buscando Elementos por posição   
    #print(listaLetras.busca('EstaLetra'))
    #print(listaInteiros.busca(13))
    print('buscando a posição de determinados nós')
    print(listaLetras.busca('UmaLetra'))
    print(listaInteiros.busca(6))
    print(separador)
    
    input(' ')
#== == == == ==Removendo    
    print('Saiu este nó: ',listaInteiros.remover(3))
    print('Saiu este nó: ',listaLetras.remover(3))
    print(listaInteiros,'\n', listaLetras)
    print(separador)
    
    input(' ')
    #print(listaInteiros.elemento(20))
    #print(listaLetras.elemento(30))
    
#== == == == Descubrindo o conteudo de elementos através da posição 
    print('descobrindo o contéudo de uma posição X \n',listaInteiros.elemento(3))
    print(listaLetras.elemento(5))
    print(separador)
    
    input(' ')

#== == == == Modificando o conteudo de elementos 
    for i in range(3):
        listaInteiros.modificar(i+1,listaInteiros.elemento(i+1) *4)
    

    
    for j in range(3):
        listaLetras.modificar(j+1,'Não é ' + listaLetras.elemento(j+1))
    
    print('Modifcano os nós\n',listaInteiros,'\n\n', listaLetras)
    print(separador)
    input(' ')

#== == == == Esvaziando a Lista

    print('esvaziando a lista \n',listaLetras.esvazia())
    print(listaInteiros.esvazia())
    #print('\n',listaInteiros,'\n\n', listaLetras)
    print(separador)
    input(' ')


#== == == == Inserido elementos depois de apagar a lista:
    print('inserindo elementos em um nó depois de tê-lo esvaziado')
    for i in range(10):
        listaInteiros.inserir(i+1,(( (i+10) * 4 +2 ) %5)-12 )
        listaLetras.inserir(i+1,'Letra '* ( ((i+1)%3)+1) )
    print(listaInteiros)
    print(listaLetras)
    print(separador)
    input(' ')
    
#== == == == Possíveis excessões    
except ListaException as LE:
    print(LE)