#from pilhaSequencial import *
from pilhaEncadeada import *

#== == == == Variáveis
separador= '\n'+('-0-0'*30)

stringsLista=['Letra','UmaLetra','OutraLetra','TerceiraLetra','QuartaLetra','23']
inteirosLista=[0,2,4,6,8,10,12,14,16,18,20,22,24,26]

#== == == == Criando as Pilhas
pilhaInteiros = Pilha()
pilhaLetras=Pilha()

#== == == == == Empilhando

for i in stringsLista:
    pilhaLetras.empilha(i)

for i in inteirosLista:
    pilhaInteiros.empilha(i)

try:
    print(pilhaInteiros)
    print(pilhaLetras)
    print(separador)
    
#== == == == == Buscando Elementos por posição   
    #print(pilhaLetras.busca('EstaLetra'))
    #print(pilhaInteiros.busca(13))
    
    print(pilhaLetras.busca('Letra'))
    print(pilhaInteiros.busca(6))
    print(separador)
    
#== == == == ==Desempilhando    
    pilhaInteiros.desempilha()
    pilhaLetras.desempilha()
    print(pilhaInteiros,'\n', pilhaLetras)
    print(separador)
    
    #print(pilhaInteiros.elemento(20))
    #print(pilhaLetras.elemento(30))
    
#== == == == Descubrindo o conteudo de elementos através da posição 
    print(pilhaInteiros.elemento(3))
    print(pilhaLetras.elemento(5))
    print(separador)
    

#== == == == Modificando o conteudo de elementos 
    for i in range(3):
        pilhaInteiros.modificar(i+1,pilhaInteiros.elemento(i+1) *4)
    

    
    for j in range(3):
        pilhaLetras.modificar(j+1,'Não é ' + pilhaLetras.elemento(j+1))
    
    print('\n',pilhaInteiros,'\n\n', pilhaLetras)
    print(separador)

#== == == == Esvaziando a Lista

    print(pilhaLetras.esvazia())
    print(pilhaInteiros.esvazia())
    #print('\n',pilhaInteiros,'\n\n', pilhaLetras)
    print(separador)

#== == == == Possíveis excessões    
except PilhaException as PE:
    print(PE)