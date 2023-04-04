import os
import time
#from filaEncadeadaNoCabeca import *
from filaSequencialCircular import *


def mostrarDicionario(dicionario:dict)->str:
    dicionarioChaves=list(dicionario.keys())
    s=''
    for i in dicionarioChaves:
        s+= f'{i :^5}=> {dicionario[i]:^5} \n'
    return s
        
opcoesFila={
    'I':'Obter informações da Fila',
    'E':'enfileira Novo Nó',
    'D':'Desenfileirar Nó',
    'V':'Verificar se está vazia',
    'M':'Modificar a carga de um Nó',
    'Q':'Descobrir a carga de um Nó apartir da posição',
    'B':'Buscar a posição de Um Nó',
    'L':'Obter a quantidade de Nós',
    'N':'Obter informações do Node Leader',
    'A': 'Esvaziar a Fila',
    '-':'Finalizar o programa'
}

F1=Fila()
#-- -- Preenchendo sozinho:
for i in range(1,17,3):
    F1.enfileira((i*3)//2)
while True:
    try:
        print()
        print("=="*30)
        print(F1)
        print("=="*30)
        
        Posicao=0
        Chave=0
        Carga=''
        print('Escolha uma das seguintes opções: ')
        print(mostrarDicionario(opcoesFila))
        escolha=str.upper(input('\n escolha: '))
#== == == == == ==
        
        if escolha== '-':
            print('Programa Finalizado')
            break  
        
        if escolha in ['M','Q']: #Escolhas que precisam de um informação
            Posicao=int(input('Digite qual a posição desejada para realizar tal operação: '))
        
        elif escolha in ['B'] : #Escolhas que precisam de uma chave
            Chave= int(input('Digite o valor da chave do Nó: '))
        
        if escolha=='I':# Informações da Fila
            print(F1)
        
        elif escolha== 'E': # enfileira um Novo nó  
            Carga= int(input('Digite a Carga do nó: '))
            F1.enfileira(Carga)
        
        elif escolha=='D':#Desenfileirar Nó
            print(F1.desenfileira())      
        
        elif escolha=='V': #Vê se a Fila está vazia
            print(F1.estaVazia())
        
        elif escolha=='M':#Modificar o Nó
            modificacao=input('Digite o valor que desja enfileira no Node: ')
            print(F1.modificar(Chave,modificacao)) 
        
        elif escolha=='Q':#Descobre o nó pela posição
            print(F1.elemento(Posicao))
        
        elif escolha=='B': #Recebe uma chave, busca a posição de um nó
            print(F1.busca(Chave))
        
        
        elif escolha=='L':# Tamanho da fila Fila
            print(len(F1))

        elif escolha=='N':# Informa o que tem no nó leader
            print(F1)
       
        elif escolha=='A':# Esvaziar a Fila
            F1.esvazia()
    
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')

    except FilaException as LE:
        os.system('clear')
        print(LE)
        time.sleep(2)
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2)