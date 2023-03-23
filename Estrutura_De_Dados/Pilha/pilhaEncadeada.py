#== == == == Pilha Exception
class PilhaException(Exception):

    def __init__(self,code, msg):
        '''
        -1: Alguma excessão que não esperada.
        0: A pilha se encontra vazia.
        1: Posição Inválida.
        2: Não foi achado o nó.
        '''
        super().__init__(f'Pilha Exception {code}: {msg}')
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.
class No :
    def __init__(self,valor) -> None:
        self.value= valor # ele possui um valor
        self.prox= None # como também um apontador
    
    def __str__(self):
        return str(self.value)
    
#== == == == A estrutura de dado Pilha, ou LIFO.
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
        '''Retorna o tamanho  da lista'''

        return self.__tamanho
    
    def __len__(self)->int:
        return self.__tamanho
    
    def getTopo(self):
        '''Retorna o primeiro nó da lista'''
        return self.__start

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        '''Retorna o valor de um elemento a partir de uma determinada posição'''
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
            raise PilhaException(1,AE)
        except Exception as E:
            raise PilhaException(-1,E)
        else:
            return valorNo

#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        '''Retorna a posição de um elemento a partir de uma chave'''
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            cursor=self.__start #cursor é quem pecorre a pilha
            cont=0
            while cont < self.__tamanho: # será percorrido ou até o final da lista ou até encontrar o contéudo.
                cont+=1
                if cursor.value == conteudo:
                    return (self.__tamanho +1) -cont        
                cursor=cursor.prox 
                
            raise PilhaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise PilhaException(2,AE)
        except Exception as E:
            raise PilhaException(-1,E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        '''Troca o valor de um nó a partir de uma determinada posição'''
        try:
            #== == Só funciona se: a pilha NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__tamanho>=posicao and posicao>0, f'Posição Inválida! A pilha possui: {self.__tamanho} nó(s)!'
            
            cursor=self.__start
            passos= self.__tamanho - posicao
            cont=1
            
            while cont <= passos:
                cursor=cursor.prox 
                cont+=1  
            
            cursor.value=conteudo
            
        except AssertionError as AE:
            raise PilhaException(1,AE)
        
        except Exception as E:
            raise PilhaException(-1,E)
        
    #== == Adiciona um novo Nó na Pilha.
    def empilha(self, conteudo:any):
        '''Insere um novo nó ao topo da lista'''
        novoNo=No(conteudo)
        novoNo.prox=self.__start
        self.__start=novoNo
        self.__tamanho +=1
    #== == Remove o Ùltimo Nó adicionado na Pilha.
    def desempilha(self)->any:
        '''Remove o nó do topo da lista.'''
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            noValor= self.__start.value
            self.__start=self.__start.prox
            self.__tamanho-=1
            return noValor
            
        except AssertionError as AE:
            raise PilhaException(0,AE)
        
        except Exception as E:
            raise PilhaException(-1,E)

    #== == Desempilha a pilha até ela possuir Zero Nós.
    def esvazia(self):
        '''Desempilha a pilha até que ela esteja completamente vazia'''
        try:
            while self.__tamanho>0:
                self.desempilha()
            
            return True
        except:
            return False
    
    
    #== == Mètodo extra 1... Concatenador de Pilhas.
    
    def concatenar(self,outraPilha):
        '''
        Empilha os elementos de uma segunda pilha
        \n P1[0,2,3,4] P2[3,4,5,7] P1.concatenar(P2)
        \n P1[3,4,5,7,0,2,3,4]
        '''
        
        pilhaAuxiliar=Pilha()
        while not outraPilha.estaVazia():
            pilhaAuxiliar.empilha(outraPilha.desempilha())
        
        while not pilhaAuxiliar.estaVazia():
            self.empilha(pilhaAuxiliar.desempilha())
    
    
    #== == Mètodo extra 2... Virar ao contrário.
    
    def inverter(self)->bool:
        '''Este método inverte a ordem da pilha, fazendo com que o topo vá para o final da pilha e visse e verça.'''
        try:
            pilhaAuxiliar=Pilha()
            while self.__tamanho>0:
                pilhaAuxiliar.empilha(self.desempilha())
                
            self.__start= pilhaAuxiliar.getTopo()
            self.__tamanho= len(pilhaAuxiliar)
            return True
        except:
            return False

    def __str__(self)->str:
        if self.__tamanho==0:
            return 'Empty'
        
        s = ''
        cont=0
        cursor=self.__start
        while cont< self.__tamanho:
            
            if cont==0: s+=f'|TOPO: {cursor}| '
            
            else:s+=f'|Nó {self.__tamanho-cont}: {cursor}| '
            
            cont+=1
            cursor=cursor.prox
        return s + f'tamanho: {self.__tamanho}'



