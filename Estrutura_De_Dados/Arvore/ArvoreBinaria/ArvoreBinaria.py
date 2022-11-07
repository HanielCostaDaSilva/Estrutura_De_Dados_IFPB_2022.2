from enum import Enum

#== == == ==Criador da Exceções da Árvore binário
class BinaryArborException(Exception):
    def __init__(self, msg) -> None:
        super().__init__('Binary Arbor Exception: ', msg)

#== == == ==Criador da Exceções dos Nós
class NodeException(Exception):
    def __init__(self, msg) -> None:
        super().__init__('Node Exception: ', msg)        
#== == == ==Aqui onde os nós são criados
class Node:
    def __init__(self,carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return str(self.carga)

#== == == ==Enumera os elementos contido  na Arvore Binária
class Origem(Enum):
    RAIZ = 1
    CURSOR = 2
    
#== == == ==Classe que contém todos os métodos aárvore binária
class ArvoreBinaria:
    #== == == Método que cria a raiz               
    def __init__(self, carga_da_raiz=None):
        self.__raiz=Node(carga_da_raiz) if carga_da_raiz != None else carga_da_raiz#== == Caso não seja declarado um nó raiz, a árvore existirá, porém vazia.
        self.__cursor= self.__raiz

    ''' Exemplo de árvore binária
                    A
                B         C
             D         E      F
          I    J         K
    '''
    @property
    def raiz(self):
        return self.__raiz
    
    @property
    def cursor(self):
        return self.__cursor
    
    #== == == Método que confere se a raiz está vazia            
    def estaVazia(self)->bool:
        if self.__raiz==None: return True
        else: return False
    
    #== == == Retorna o Nó raiz, caso ele exista            
    def getRaiz(self)->any:
        try:
            assert self.__raiz != None 
            return self.__raiz
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

     #== == == Retorna o nó que está sendo apontado pelo cursor            
    def getCursor(self)->any:
        try:
            assert self.__raiz != None
        
            return self.__cursor
        except AssertionError:
            raise BinaryArborException('NO ROOT!')
    
    #== == == Retorna os elementos em préordem
    '''Pré-Ordem: Mostra o nó e depois se dirige para a sua esquerda, depois prossegue para a direita.
    Este seria a amostragem da pré-odem da árvore do começo: IDJBAEKCF'''            
    def preordem(self, origem:Origem=Origem.RAIZ):
        try:
            assert not(self.estaVazia())
            if origem==Origem.RAIZ.value: self.__preordem(self.__raiz)
            elif origem==Origem.CURSOR.value: self.__preordem(self.__cursor)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')
    
    def __preordem(self, no:Node):
        if no==None:
            return
        print(no.carga)
        self.__preordem(no.esq)
        self.__preordem(no.dir)
        
    #== == == Retorna os elementos em in-ordem
    '''In-Ordem: Se Dirige para extrema esquerda, Mostra o Nó, depois mostra o Nó acima e prossegue para a sua direita.
    Este seria a amostragem da in-odem da árvore do começo: ABDIJCEK'''            
    def emordem(self, origem:Origem=Origem.RAIZ.value):
        try:
            assert not(self.estaVazia())
            if origem==Origem.RAIZ.value: self.__emordem(self.__raiz)
            elif origem==Origem.CURSOR.value: self.__emordem(self.__cursor)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')


    def __emordem(self, no:Node):
        if no==None:
            return
        self.__emordem(no.esq)
        print(no)
        self.__emordem(no.dir)
        
    #== == == Retorna os elementos em pós-ordem
    '''Pós-Ordem: Dirige-se para a direita e depois para esquerda. Em seguida, mosta o nó
    Este seria a amostragem da pré-odem da árvore do começo: FKECJIDBA'''      
    def posordem(self, origem:Origem=Origem.RAIZ.value):
        try:
            assert not(self.estaVazia())
            if origem==Origem.RAIZ.value: self.__posordem(self.__raiz)
            elif origem==Origem.CURSOR.value: self.__posordem(self.__cursor)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

    def __posordem(self, no:Node):
        if no==None:
            return
        self.__posordem(no.dir)
        self.__posordem(no.esq)
        print(no)
        #== == == Move o cursor para a equerda do nó      
    def descerEsquerda(self):
        try:
            assert not(self.estaVazia())
            if self.__cursor.esq==None:
                raise(f'O cursor está no Nó: {self.__cursor.carga} ele não possui Nó à esquerda!')
            self.__cursor=self.__cursor.esq
        except AssertionError:
            raise BinaryArborException('NO ROOT!')
        
    #== == == Move o cursor para a direita do nó 
    
    def descerDireita(self):
        try:
            assert not(self.estaVazia())
            if self.__cursor.dir==None:
                raise(f'O cursor está no Nó: {self.__cursor.carga} ele não possui Nó à direita!')
            self.__cursor=self.__cursor.dir
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

#== == == Move o cursor de volta para a raiz. 
    def resetCursor(self):
        try:
            assert not(self.estaVazia())
            self.__cursor= self.__raiz
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

#== == == Insere um nó a equerda do cursor. 
    def addFilhoEsquerdo(self, carga)->bool:
        try:
            assert not(self.estaVazia())
            if self.__cursor.esq!=None:
                raise NodeException('THERE IS A NODE AT LEFT')
            
            self.__cursor.esq=Node(carga)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

#== == == Insere um nó a direita do cursor.     
    def addFilhoDireito(self, carga)->bool:
        
        try:
            assert not(self.estaVazia())
            if self.__cursor.dir!=None:
                raise NodeException('THERE IS A NODE AT RIGHT')
            
            self.__cursor.dir=Node(carga)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')

    #== == == Retorna a quantiade de Nós
    
    def __len__(self):
        return self.__count(self.__raiz)
    
    
    def __count(self, no:Node)->int:

        if no==None:
            return 0 #== == Chegou ao fim.
        
        quantidadeNo= 1 +self.__count(no.esq) # quantidade nó é criado e é somado com a quantiade de nós a sua  do nó a esquerda
        quantidadeNo+= self.__count(no.dir) # quando não há nós a esquerda, ele tentará a sua direita.
        return quantidadeNo #finalizado, ele retornará a soma.

    #se orientado ao cursor
    def busca(self, chave,origem):
        try:
            assert not(self.estaVazia())
            if origem== Origem.RAIZ.value: self.__busca(chave,self.__raiz)
            elif origem== Origem.CURSOR.value: self.__busca(chave,self.__cursor)
        except AssertionError:
            raise BinaryArborException('NO ROOT!')
    
    #== == == == procura se existe um determinado. se orientando pelo cursor
    def __busca(self, chave, node:Node) ->bool:
        
        if node==None: # não achou o nó
            return False
        
        elif node.carga==chave:
            return True
        
        elif self.__busca(chave,node.esq): #busca pela esquerda
            return True
        
        elif self.__busca(chave,node.dir): #busca pela direita
            return True
    
    #== == == Esse método é orientado ao cursor. Ele excluir o nó a direita ou a esquerda do cursor
    def removeNoFolha(self,chave):
        try:
            assert not(self.estaVazia())
            #== == Testa se o nó á ser removido esquerda
            if self.__cursor.esq!= None:
                
                if self.__cursor.esq.carga==chave and \
                self.__cursor.esq.esq ==None and self.__cursor.esq.dir==None:
                
                    self.__cursor.esq= None  #== O nó que o cursor está apontará para o None em sua esquerda.
                
                else:
                    raise BinaryArborException('THIS NOT A LEAF NODE')         
            
            #== == Testa se o nó da direita é nó folha
            elif self.__cursor.dir!=None:
                if self.__cursor.dir.carga==chave and \
                    self.__cursor.dir.esq== None and self.__cursor.dir.dir==None:
                        self.__cursor.dir= None
                
                else:
                    raise BinaryArborException('THIS NOT A LEAF NODE')
            
            else:
                raise BinaryArborException('KEY NOT FOUND')
        
        except AssertionError:
            raise BinaryArborException('NO ROOT!')   
        
        
    def go(self, chave:int )->Node:
        return self.__go(chave,self.__raiz)
    
    def __go(self, chave:int, Node:Node)->Node:
        if Node is None:
            return None
        if Node.carga == chave:
            return Node
        resultado = self.__go(chave, Node.esq)
        if ( resultado ):
            return resultado
        else:
            return self.__go(chave, Node.dir)

    
    #== == == Método que remove todos os nós de maneira que não deixe vestígios na memória 
    def esvazia(self):
        try:
            assert not(self.estaVazia())
            self.__raiz=self.__libera(self.__raiz)
            
        except AssertionError:
            raise BinaryArborException('NO ROOT!')
        
    def __libera(self,proximoNo)->None:
        
        if ( not self.estaVazia() and proximoNo != None):
            
            proximoNo.esq= self.__libera(proximoNo.esq)
            
            proximoNo.dir= proximoNo=self.__libera(proximoNo.dir)
        return None
    
    def adicionarRaiz(self,NodeCarga:Node):
        try:
            assert self.estaVazia()
            self.__raiz=Node(NodeCarga)
            self.__cursor=self.__raiz
        except AssertionError:
            raise BinaryArborException('THERE IS A ROOT')
        
    #== == == Método que mostra a quantidade de nós folhas presente na árvore
    def leafs(self):
        try:
            assert not( self.estaVazia())
            return self.__leafs(self.__raiz)
        except AssertionError:
            raise BinaryArborException('THERE IS NOT A ROOT')
    
    
    def __leafs(self,proximoNo:Node):
        leafsQuanty=0
        if proximoNo==None: #== == Só por precaução...
            return leafsQuanty
        if proximoNo.dir==None and proximoNo.esq==None:
            return 1
        leafsQuanty+=self.__leafs(proximoNo.esq)
        leafsQuanty+=self.__leafs(proximoNo.dir)
        return leafsQuanty
    
    def profundidade(self):
        try:
            assert not( self.estaVazia())
            return (self.__profundidade(self.__raiz) -1)
        except AssertionError:
            raise BinaryArborException('THERE IS NOT A ROOT')
        
    def __profundidade(self, proximoNo:Node):
        alturaEsquerda=0
        alturaDireita=0
        if proximoNo==None:
            return 0
        alturaEsquerda= 1 + self.__profundidade(proximoNo.esq)
        alturaDireita= 1 + self.__profundidade(proximoNo.dir)
        return (max(alturaEsquerda,alturaDireita))
