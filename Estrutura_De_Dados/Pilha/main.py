import os
import time
from pilhaEncadeada import *
#from pilhaSequencial import *

def decToBin( numero:int):
    pilhaAuxiliar=Pilha()
    while numero>=0:
        resto=numero%2
        numero=numero//2
        pilhaAuxiliar.empilha(str(resto))
        if numero==0:
            break
    
    numeroBinario=''
    while not(pilhaAuxiliar.estaVazia()):
        numeroBinario+= pilhaAuxiliar.desempilha()
    
    return int(numeroBinario)


def mostrarDicionario(dicionario:dict)->str:
    dicionarioChaves=list(dicionario.keys())
    s=''
    for i in dicionarioChaves:
        s+= f'{i :^5}=> {dicionario[i]:^5} \n'
    return s


def MostrarDicionario(dicionario:dict, chaveBusca:str = '0'):
    '''
    Este método recebe um dicionário e uma lista contendo suas chavesBusca, em seguida mostra-o na tela de maneira formatada 
    '''
    if dicionario.get(chaveBusca,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{chaveBusca :^5}=> {dicionario[chaveBusca]:^5} ')
    MostrarDicionario(dicionario, str(int(chaveBusca) +1 ) )
        
opcoesPilha={
    'I':'Informações da Pilha',#0
    'E':'Empilhar Novo Nó',#1
    'D':'Desempilhar Nó',#2
    'V':'Verificar se está vazia',#3
    'M':'Modificar a carga de um Nó',#4
    'P':'Procurar Nó apartir da posição',#5
    'B':'Buscar a posição de Um Nó',#6
    'T':'Tamanho Pilha',#7
    'L':'Limpar a Pilha',#8
    'C': 'Inverter Ordem da Pilha',#9
    'N':'Escolher Outra Pilha',#10
    'U':'Conversão dec/bin',
    'F':'Finalizar o programa'#-
    
}
opcoesPilhachavesBusca= list(opcoesPilha.keys())

pilhasLista=[None for i in range(10)]# O programa será multipilhas.
posicaoPilhaAtual=0 #Posicao em que o usuario se encontra atualmente.


#-- -- Preenchendo a Lista de Pilhas:

for i in range(10):
    pilhasLista[i]=Pilha()
    #-- -- Preenchendo automaticamente a Pilha
    for j in range(i,i*6,3):
        pilhasLista[i].empilha((j*3)//2)

while True:
    try:
        pilhaAtual=pilhasLista[posicaoPilhaAtual]
        chaveBusca=0
        posicaoNode=0
        
        print("=="*30)
        print(f"Pilha selecionada: {posicaoPilhaAtual+1} de {len(pilhasLista) } Pilhas. ")
        print(pilhaAtual)
        print("=="*30)
 
        
        print('Escolha uma das seguintes opções: ')
        print(mostrarDicionario(opcoesPilha))
        escolha=str.upper(input('\n escolha: '))
        

        if escolha=='F':#== == == Encerra o programa
            break
          
        
        if escolha  in ['M','P']: #Escolhas que precisam de um informação
            posicaoNode=int(input('Digite qual a posição desejada para realizar tal operação: '))
        
        if escolha=='B' : #Escolhas que precisam de uma chaveBusca
            chaveBusca= int(input('Digite o valor que procuras do Nó: '))
        
        if escolha=='I':# Informações da Pilha
            print(pilhaAtual)
        
        elif escolha== 'E': # empilha um Novo nó
            Carga=int(input('Digite um valor inteiro a ser inserido: '))
            pilhaAtual.empilha(Carga)
        
        elif escolha=='D':#Desempilhar Nó
            print(pilhaAtual.desempilha())      
        
        elif escolha=='V': #Vê se a Pilha está vazia
            print(pilhaAtual.estaVazia())
        
        elif escolha=='M':#Modificar o Nó
            modificacao=int(input('Digite o valor que desja modificar no Node: '))
            pilhaAtual.modificar(posicaoNode,modificacao)
        
        elif escolha=='P':#Descobre o nó pela posição
            print(pilhaAtual.elemento(posicaoNode))
        
        elif escolha=='B': #Recebe uma chaveBusca, busca a posição de um nó
            print(pilhaAtual.busca(chaveBusca))
        
        
        elif escolha=='T':# Tamanho da Pilha
            print(len(pilhaAtual))

       
        elif escolha=='L': #Limpar a Pilha
            print(pilhaAtual.esvazia())
            
        elif escolha=='C': #Inverter Ordem da Pilha
            pilhaAtual.inverter()
            
        
        elif escolha=='N': #Escolher Outra Pilha
            posicaoPilhaAtual=int(input(f"[1 - {len(pilhasLista)}] Digite qual posição deseja acessar: "))-1
            if posicaoPilhaAtual> len(pilhasLista) or posicaoPilhaAtual<0: 
                posicaoPilhaAtual=0
                raise Exception("Posição de pilha inserida é inválida! ")
        
        elif escolha=='U':#Conversão dec/bin
            numeroDecimal= int(input('Digite o valor que desejas ser convertido para binário: '))
            
            print(decToBin(numeroDecimal))
            
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')


    except PilhaException as LE:
        os.system('clear')
        print(LE)
        time.sleep(2)
    
    except TypeError as TE:
        os.system('clear')
        print(TE)
        time.sleep(2)
    
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2)
        