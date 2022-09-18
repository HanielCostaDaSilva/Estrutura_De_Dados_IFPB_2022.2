#== == == == Pilha Exception
class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.
class No :
    def __init__(self,valor) -> None:
        self.value= valor # ele possui um valor
        self.prox= None # como também um apontador
    
    def __str__(self):
        return str(self.value)
    
#== == == == A estrutura de dado Pilha, ou FIFO.
class Pilha:
    def __init__(self):
        self.__start= None  #Seu primeiro elemento é None, até receber nós
        self.__tamanho=0 #Ela inicia vazia

#== == == == Método para examinar se a pilha está vazia
    def estaVazia(self)->bool:
        return self.__tamanho == 0
    
#== == == == Método para checar o tamanho da Pilha
    @property
    def tamanho(self)->int:
        return self.__tamanho

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a pilha NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__tamanho>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da pilha é de {self.__tamanho} nó(s)!'
            
            cursor=self.__start #Cursor é quem percorrerá cada nó, ele inicia no topo da Pilha
            valorNo=cursor.value #valorNo é a variável que armazena o valor
            passos= self.__tamanho - posicao #passos é a quantidade de nós que o cursor percorrerá
            cont=1
            
            while cont <= passos:
                cursor=cursor.prox
                valorNo=cursor.value
                cont+=1
        
        except AssertionError as AE:
            raise PilhaException(AE)
        except Exception as E:
            raise PilhaException(E)
        else:
            return valorNo

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            cursor=self.__start #cursor é quem pecorre a pilha
            cont=0
            while cont < self.__tamanho: # será percorrido ou até o final da lista ou até encontrar o contéudo.
                cont+=1
                if cursor.value == conteudo:
                    return cont        
                cursor=cursor.prox 
                
            raise PilhaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise PilhaException(AE)
        except Exception as E:
            raise PilhaException(E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        try:
            #== == Só funciona se: a pilha NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__tamanho>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da pilha é de {self.__tamanho} nó(s)!'
            
            cursor=self.__start
            passos= self.__tamanho - posicao
            cont=1
            
            while cont <= passos:
                cursor=cursor.prox 
                cont+=1  
            
            cursor.value=conteudo
            
        except AssertionError as AE:
            raise PilhaException(AE)
        
        except Exception as E:
            raise PilhaException(E)
        
    #== == Adiciona um novo Nó na Pilha.
    def empilha(self, conteudo:any):
        novoNo=No(conteudo)
        novoNo.prox=self.__start
        self.__start=novoNo
        self.__tamanho +=1
    #== == Remove o Ùltimo Nó adicionado na Pilha.
    def desempilha(self)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            
            self.__start=self.__start.prox
            self.__tamanho-=1
            
        except AssertionError as AE:
            raise PilhaException(AE)
        
        except Exception as E:
            raise PilhaException(E)

    #== == Desempilha a pilha até ela possuir Zero Nós.
    def esvazia(self):
        try:
            while self.__tamanho>0:
                self.desempilha()
        except:
            pass


    def __str__(self)->str:
        if self.__tamanho==0:
            return 'Empty'
        s = ''
        cont=0
        cursor=self.__start
        while cont< self.__tamanho:
            s+=f'|Nó {self.__tamanho-cont}: {cursor}| '
            cont+=1
            cursor=cursor.prox
        return s + f'tamanho: {self.__tamanho}'
