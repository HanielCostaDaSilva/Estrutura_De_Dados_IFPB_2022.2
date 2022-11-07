from ArvoreBinaria import ArvoreBinaria,NodeException, BinaryArborException
import time
import os

#== == == == Exemplo pronto
arv = ArvoreBinaria(12)
arv.addFilhoDireito(13)
arv.addFilhoEsquerdo(11)
arv.descerDireita()
arv.addFilhoDireito(15)
arv.addFilhoEsquerdo(18)
arv.descerEsquerda()
arv.addFilhoEsquerdo(19)
arv.resetCursor
arv.descerEsquerda()
arv.addFilhoDireito(21)
arv.addFilhoEsquerdo(22)

#== == == == Funções
def MostrarDicionario(dicionario:dict, Chave:str = '1'):

    if dicionario.get(Chave,False)==False:
        print(f'{"-":^5}=> {dicionario["-"]:^5} ')
        return
    print(f'{Chave :^5}=> {dicionario[Chave]:^5} ')
    MostrarDicionario(dicionario, str(int(Chave) +1 ) )
        

opcoesArvore={
    '1':'Mostrar Nós em Pré-Ordem',
    '2':'Mostrar Nós em In-Ordem',
    '3':'Mostrar Nós em Pós-Ordem',
    '4':'Mostrar o Valor da Raiz',
    '5':'Mostrar o Valor do Cursor',
    '6':'Mover o Cursor para esquerda',
    '7':'Mover o Cursor para direita',
    '8':'Adicionar Nó a esquerda',
    '9':'Adicionar Nó a direita',
    '10':'Buscar se existe um Nó.',
    '11':'Remover Nó folha.',
    '12':'Mover o cursor atrás de um nó específico',
    '13':'Esvaziar a Árvore',
    '14':'Mostrar o tamanho da árvore',
    '15': 'Mover o cursor para raiz',
    '16': 'Adicionar Nó raiz',
    '17': 'Contar a quantidade de nós folhas',
    '18': 'Contar a profundidade',
    '-':'finalizar o programa',
}

opcoesArvoreChaves= list(opcoesArvore.keys())
while True:
    try:
        print()
        print('Escolha uma das seguintes opções: ')
        MostrarDicionario(opcoesArvore)
        escolha=input('\n escolha: ')
#== == == == == ==        
        if escolha== '1' or escolha== '2' or escolha== '3' or escolha=='10'  or escolha=='11':
            
            origem= str.lower(input('Digite a Origem: (raiz/cursor) '))
            if origem=='raiz':
                origem=1
            elif origem=='cursor':
                origem=2
            else:
                raise(Exception('por favor, escolha: raiz ou cursor '))
            
            if escolha=='1': #== == == Mostra a árvore em pré-ordem
                arv.preordem(origem)
            
            elif escolha=='2':#== == == Mostra a árvore em in-ordem
                arv.emordem(origem)
            
            elif escolha=='3':#== == == Mostra a árvore em pós-ordem
                arv.posordem(origem)
                
            elif escolha=='10' or escolha=='11': 
                NodeValue= input('digite o valor do Nó: ')
                
                if escolha=='10':
                    arv.busca(NodeValue,origem)
                if escolha=='11': #== == == Procura a existência de um nó à partir de uma determinada origem
                    arv.busca(NodeValue,origem)
            
        
        elif escolha=='4': #== == == Mostra o valor da raiz
            print(arv.getRaiz())
            
        elif escolha=='5': #== == == Mostra o valor do cursor
            print(arv.getCursor())
        
        elif escolha=='6': #== == == Move o cursor à sua esquerda
            print(arv.descerEsquerda())
        
        elif escolha=='7': #== == == Move o cursor à sua direita
            print(arv.descerDireita())

#== == == == == ==
        elif escolha=='8' or escolha=='9' or escolha=='12' or escolha=='16':
            NodeValue= input('digite o valor do Nó: ')
            
            if escolha=='8': #== == == Adiciona um nó à esquerda do cursor
                arv.addFilhoEsquerdo(NodeValue)
                print(f'Nó {NodeValue} adicionado a esquerda!')
            
            elif escolha=='9': #== == == Adiciona um nó à direita do cursor
                arv.addFilhoDireito(NodeValue)
                print(f'Nó {NodeValue} adicionado a direita!')
            
            elif escolha=='12': #== == == Move o cursor para um determinado nó
                arv.go(NodeValue)
                print(f'Cursor movido para o Nó {NodeValue}!')
                    
            elif escolha=='16':#== == == Adiciona uma raiz
                arv.adicionarRaiz(NodeValue)
                print('Raiz criada com sucesso!')
           
        elif escolha=='13': #== == ==Esvazia a árvore
            print(arv.esvazia())
        
        elif escolha=='14':#== == == Mostra a quantidade de Nós
            print('Quantidade de nós até agora: ', arv.__len__())
        
        elif escolha=='15':#== == == Reseta o cursor
           arv.resetCursor()
           print('cursor movido para a raiz, com sucesso!')
        
        elif escolha=='17':#== == == Reseta o cursor
            print('Quantidade de nós folhas: ',arv.leafs())
                
        elif escolha=='18':#== == == Reseta o cursor
            print('Altura: ',arv.profundidade())           #=======ERRRO! CONTANDO A MAIOR QUANTIDADE DE NÒS


        elif escolha=='-':#== == == Encerra o programa
            break
        else:
            raise(Exception('CHOICE NOT FOUND'))
        input()
        os.system('clear')

    except NodeException as NE:
        os.system('clear')
        print(NE)
        time.sleep(2)

    except BinaryArborException as BAE:
        os.system('clear')
        print(BAE)
        time.sleep(2)
    except Exception as E:
        os.system('clear')
        print(E)
        time.sleep(2)
        
'''
arv = ArvoreBinaria(2)
print('Criada a árvore')
arv.addFilhoEsquerdo(7)
arv.addFilhoDireito(5)
print('Raiz: ', arv.getRaiz())
print('Cursor: ', arv.getCursor())
print('Tamanho: ', len(arv))
arv.descerEsquerda()
arv.addFilhoEsquerdo(9)
arv.descerEsquerda()
arv.addFilhoDireito(3)

print('Raiz: ', arv.getRaiz())
print('Cursor: ', arv.getCursor())
print('Tamanho: ', len(arv))

arv.resetCursor()
arv.descerDireita()
arv.addFilhoEsquerdo(10)

print()
arv.preordem()

print('Raiz: ', arv.getRaiz())
print('Cursor: ', arv.getCursor())
print('Tamanho: ', len(arv))

print('Busca:', arv.busca(3))
no = arv.go(3)
print('go:', no)'''