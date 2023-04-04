#== == == == Fila Exception
class FilaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        
#== == == == No é o elemento que será adiciona na estrutura de dados encadeada.

#== == == == A estrutura de dado Fila, ou FIFO.

class Fila:
    __tamanhoLimite=15
    __nosInseridoQuantidade=0
    
    def __init__(self):
        
        self.__fila=[None for i in range(self.__tamanhoLimite)] # A fila inicia vazia .
        self.__primeiroPosicao=0
        self.__ultimoPosicao= -1

#== == == == Método para examinar se a Fila está vazia
    def estaVazia(self)->bool:
        return len(self.__fila) == 0
    
#== == == == Método para checar o tamanho da Fila

#== == Checa a quantidade de nós inserido
    def __len__(self):
        return self.__nosInseridoQuantidade
    
#== == Checa o tamanho Máximo    
    def tamanho(self):
        return self.__nosInseridoQuantidade

#== == == == Método que retornára o contéudo de um nó dependendo da possição exigida.
    def elemento(self, posicao:int)->any:
        try:
            #== == Só funciona se: a Fila NÃO estiver vazia e a posição inserida não exceda o tamanho limite da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__len__()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da Fila é de {self.__len__()} nó(s)!'
            
            return self.__fila[posicao]
        
        except AssertionError as AE:
            raise FilaException(AE)
        except Exception as E:
            raise FilaException(E)


#== == == == Método que retornára a posição de um Nó através do valor no qual foi inserido.
    def busca(self, conteudo:any)->int:
        try:
            #== == O método só não funciona quando a lista estiver vazia
            assert not self.estaVazia() ,'A lista está vazia!'
            cont=1
            cursorPosicao=self.__primeiroPosicao
            while cont < self.__len__():
                
                if self.__fila[cursorPosicao] == conteudo:
                    return cont
    
                cursorPosicao+=1
                cont+=1
                
                if cursorPosicao % self.tamanho() ==0: #para o contador voltar ao inicio da fila
                    cursorPosicao=0
            
            raise FilaException('Contéudo inserido não foi encontrado!') # o contéudo não foi Achado.
    
        except AssertionError as AE:
            raise FilaException(AE)
        except Exception as E:
            raise FilaException(E)
                
##== == == == Método que Modificará o contéudo de um nó a partir da possição exigida.
    def modificar(self, posicao:int, conteudo: any):
        try:
            #== == Só funciona se: a fila NÃO estiver vazia e a posição inserida não exceda o tamanho da lista.
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__len__()>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da fila é de {self.__len__()} nó(s)!'
        
            self.__fila[posicao-1]= conteudo
 
        except AssertionError as AE:
            raise FilaException(AE)
        
        except Exception as E:
            raise FilaException(E)
        
    #== == Adiciona um novo Nó na fila.
    def enfileira(self, conteudo:any):
        try:
            assert self.__nosInseridoQuantidade < self.__tamanhoLimite, 'A fila está cheia!'
            
            self.__ultimoPosicao=(self.__ultimoPosicao+1)%self.__tamanhoLimite
            
            self.__fila.insert(self.__ultimoPosicao,conteudo)
            
            self.__nosInseridoQuantidade+=1
        
        except AssertionError as AE:
            raise FilaException(AE)
        
        except Exception as E:
            raise FilaException(E) 
        
    #== == Remove o primeiro Nó adicionado na Fila.
    def desenfileira(self)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            valorStartNo=self.__fila[self.__primeiroPosicao] #È necessário coletar o valor do Primeiro e então removê-lo da fila.
            self.__fila[self.__primeiroPosicao]=None
            
            if self.__primeiroPosicao == self.tamanho()-1:
                self.__primeiroPosicao=0
            else:
                self.__primeiroPosicao += 1

            self.__nosInseridoQuantidade-=1
            return valorStartNo
            
        except AssertionError as AE:
            raise FilaException(AE)
        
        except Exception as E:
            raise FilaException(E)

    #== == Desenfila a fila até ela possuir Zero Nós.
    def esvazia(self):
        try:
            while self.__nosInseridoQuantidade>0:
             self.desenfileira()
        except:
            pass


    def __str__(self)->str:
        if self.__nosInseridoQuantidade==0:
            return 'Empty'
        s = 'Fila Sequencial Circular \n'
        
        cursorPosicao=self.__primeiroPosicao
        cont=0

        while cont < self.__len__():
            
            s += f' =|{cont + 1}: {self.__fila[cursorPosicao]}|= '
            
            cursorPosicao+=1
            cont+=1    
            if cursorPosicao % self.tamanho() ==0: #para o contador voltar ao inicio da fila
                cursorPosicao=0

        return s + f'\n Nós inseridos até agora: {self.__nosInseridoQuantidade}'