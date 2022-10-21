from ArvoreBinaria import *

#== == == == Este método percorrera toda a árvore execultando primeiramente dá raiz e em seguida da esquerda de todos os nós
def preordem(no_inicial):
    if no_inicial is None: # Se Chegar a um nó folha
        return # não faz nada
    print(f'{no_inicial.carga}', end=' ')
    preordem(no_inicial.esq) #== == == Ele execultará até a última esquerda do nó
    preordem(no_inicial.dir)#== == == Quando terminar de percorrer a esquerda de um nó, ele então irá percorrer a direita deste

#== == == == Esta busca inicirá sempre da folha a mais esquerda. 
def emordem(no_inicial):
    if no_inicial is None: #Se chegar a um nó folha
        return # encerra a recursividade
    emordem(no_inicial.esq) #ela execultará a recursividade até que chegue no nó mais a esquerda 
    print(f'{no_inicial.carga}', end=' ') #caso já tenha percorrido o nó mais esquerda deste execultára algum comoando
    emordem(no_inicial.dir) #agora percorrerá a sua direita


#== == == == Esta busca inicirá sempre no nó folha mais extremo, inicia sempre pela esquerda. 
def posordem(no_inicial): 
    if no_inicial is None: #chegou no nó mais extremo
        return #termina a recursividade
    posordem(no_inicial.esq) #primeiro, busca se a algum nó a esquerda do estudado
    posordem(no_inicial.dir) #depois, vê se não a nenhum outro a direita
    
    print(f'{no_inicial.carga}', end=' ') # caso as duas condições acima sejam atendidas, ou já tenha sido execultada as suas extremidades, o nó será executado. 

#== == == == Essa é a busca mais simples, o usuário passa uma chave e então o programa percorrerá toda árvore em busca da chave. 
def busca(chave, no_inicial)->bool:
    if no_inicial is None:
        return False
    if no_inicial.carga == chave:
        return True
    if ( busca(chave, no_inicial.esq)):
        return True
    else:
        return busca(chave, no_inicial.dir)

raiz = No(10)
raiz.esq = No(32)
raiz.dir = No(23)
cursor = raiz.esq # cursor desce para o nó 32
cursor.esq = No(12)
cursor.dir = No(40)
cursor = cursor.esq
cursor.esq = No(5)
cursor = raiz.dir # cursor desce para o nó 23, a partir do raiz
cursor.dir = No(30)
cursor = cursor.dir # cursor desce para o nó 30
cursor.esq = No(60)
cursor = cursor.esq # cursor desce par ao nó 60
cursor.dir = No(22)

preordem(raiz)
print()
emordem(raiz)
print()
posordem(raiz)



