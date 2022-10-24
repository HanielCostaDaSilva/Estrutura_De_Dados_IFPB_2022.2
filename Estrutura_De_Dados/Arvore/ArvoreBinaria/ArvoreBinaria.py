#== == == == Onde os elementos da árvore são criados
class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None
 
    def __str__(self):
        return f'{self.carga}'
 
 
class Arvore:
    def __init__(self,valorInicial= None) -> None:
        self.__raiz= No(valorInicial) if valorInicial!= None else valorInicial
        self.__cursor= self.__raiz
    
    def preordem(self):
        if self.__cursor is None: # Se Chegar a um nó folha
            return # não faz nada
        self.preordem(self.__cursor.esq) #== == == Ele execultará até a última esquerda do nó
        self.preordem(self.__cursor.dir)#== == == Quando terminar de percorrer a esquerda de um nó, ele então irá percorrer a direita deste
 
    def emordem(self):
        if self.__cursor is None: #Se chegar a um nó folha
            return # encerra a recursividade
        self.emordem(self.__cursor.esq) #ela execultará a recursividade até que chegue no nó mais a esquerda 
        self.emordem(self.__cursor.dir) #agora percorrerá a sua direita
 
#== == == == Esta busca inicirá sempre no nó folha mais extremo, inicia sempre pela esquerda. 
    def posordem(self): 
        if self.__cursor is None: #chegou no nó mais extremo
            return #termina a recursividade
        self.posordem(self.__cursor.esq) #primeiro, busca se a algum nó a esquerda do estudado
        self.posordem(self.__cursor.dir) #depois, vê se não a nenhum outro a direita
         
 
#== == == == Essa é a busca mais simples, o usuário passa uma chave e então o programa percorrerá toda árvore em busca da chave.    
    def busca(self, chave)->bool:
        if self.__cursor is None:
            return False
        if self.__cursor.carga == chave:
            return True
        if ( self.busca(chave, self.__cursor.esq)):
            return True
        else:
            return self.busca(chave, self.__cursor.dir)
 
    def estaVazia(self):
        if self.__raiz== None:
            return True
        else: 
            return False
    
    def getRaiz(self):
        if self.__raiz != None:
            return self.__raiz.carga;
        else: return None
    
    def get__cursor(self):
        return self.__cursor
    
    def descer_A_Esquerda(self):
        if not(self.estaVazia()) and self.__cursor.esq != None:
                self.__cursor= self.__cursor.esq
    
    def descer_A_Direita(self):
        if not(self.estaVazia()):
            if self.__cursor.dir != None:
                self.__cursor= self.__cursor.dir
    
    def resetCursor(self):
        if not(self.estaVazia):
            self.__cursor=self.__raiz
 
    def count(self,cursor):
        contador=0
        if self.__cursor is None:
            return 0
 
        contador+=self.count(self.__cursor.esq) #primeiro, busca se a algum nó a esquerda do estudado
        contador+=self.count(self.__cursor.dir) #depois, vê se não a nenhum outro a direita        
        return contador + 1
 
    def __len__(self):
        return self.count()
    
    def criarRaiz(self, valor:any):
        if self.__raiz is None:
            self.__raiz== No(valor)
 
#== == == == Onde os elementos da árvore são criados
class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None
 
    def __str__(self):
        return f'{self.carga}'
 
 
class Arvore:
    def __init__(self,valorInicial= None) -> None:
        self.__raiz= No(valorInicial) if valorInicial!= None else valorInicial
        self.__cursor= self.__raiz
    
    def preordem(self):
        if self.__cursor is None: # Se Chegar a um nó folha
            return # não faz nada
        self.preordem(self.__cursor.esq) #== == == Ele execultará até a última esquerda do nó
        self.preordem(self.__cursor.dir)#== == == Quando terminar de percorrer a esquerda de um nó, ele então irá percorrer a direita deste
 
    def emordem(self):
        if self.__cursor is None: #Se chegar a um nó folha
            return # encerra a recursividade
        self.emordem(self.__cursor.esq) #ela execultará a recursividade até que chegue no nó mais a esquerda 
        self.emordem(self.__cursor.dir) #agora percorrerá a sua direita
 
#== == == == Esta busca inicirá sempre no nó folha mais extremo, inicia sempre pela esquerda. 
    def posordem(self): 
        if self.__cursor is None: #chegou no nó mais extremo
            return #termina a recursividade
        self.posordem(self.__cursor.esq) #primeiro, busca se a algum nó a esquerda do estudado
        self.posordem(self.__cursor.dir) #depois, vê se não a nenhum outro a direita
         
 
#== == == == Essa é a busca mais simples, o usuário passa uma chave e então o programa percorrerá toda árvore em busca da chave.    
    def busca(self, chave)->bool:
        if self.__cursor is None:
            return False
        if self.__cursor.carga == chave:
            return True
        if ( self.busca(chave, self.__cursor.esq)):
            return True
        else:
            return self.busca(chave, self.__cursor.dir)
 
    def estaVazia(self):
        if self.__raiz== None:
            return True
        else: 
            return False
    
    def getRaiz(self):
        if self.__raiz != None:
            return self.__raiz.carga;
        else: return None
    
    def get__cursor(self):
        return self.__cursor
    
    def descer_A_Esquerda(self):
        if not(self.estaVazia()) and self.__cursor.esq != None:
                self.__cursor= self.__cursor.esq
    
    def descer_A_Direita(self):
        if not(self.estaVazia()):
            if self.__cursor.dir != None:
                self.__cursor= self.__cursor.dir
    
    def resetCursor(self):
        if not(self.estaVazia):
            self.__cursor=self.__raiz
 
    def count(self,cursor):
        contador=0
        if self.__cursor is None:
            return 0
 
        contador+=self.count(self.__cursor.esq) #primeiro, busca se a algum nó a esquerda do estudado
        contador+=self.count(self.__cursor.dir) #depois, vê se não a nenhum outro a direita        
        return contador + 1
 
    def __len__(self):
        return self.count()
    
    def criarRaiz(self, valor:any):
        if self.__raiz is None:
            self.__raiz== No(valor)
 
 
 
 

