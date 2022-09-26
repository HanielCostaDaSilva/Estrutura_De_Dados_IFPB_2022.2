from xmlrpc.client import boolean


class NotacaoException(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class NotacaoPosfixa:
    #== == == == Atributos de toda Notação pósfixa
    __prioridadesOperadores={
        ')':0,
        '(':1,
        '+':2,
        '-':2,
        '/':3,
        '*':3,
        '^':4
    }
    __prioridadesOperadoresChaves= [*__prioridadesOperadores]
    
    __saida=''
    __operacaoPilha=[]
    __prioridadeTopo=0
    
    def conferirSeELetra(self, termo):
        if termo in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ': return True
        else: return False
        
    
    def conferirSeEOperador(self,termo):
        if termo in self.__prioridadesOperadoresChaves: return True
        else: return False  
    
    def receberOperacao(self, operacao:str)->None:
        #Método que recebe uma operação e envia uma mensagem de erro caso encontre algo anormal
        operacaoLista= list(operacao.upper())
        try:
            parentesesAberto=0
            termoAnterior=''
            for termo in operacaoLista:
                assert self.conferirSeELetra(termo) or self.conferirSeEOperador(termo), f'Não é permitido o seguinte termo inserido: {termo}. '
                
                if termo=='(':
                    parentesesAberto +=1
                    
                if termo==')':
                    if parentesesAberto == 0:
                        raise NotacaoException('foi recebido ")" sendo que não foi inserido nenhum "(" antes.')
                    parentesesAberto -=1
                
                
                if operacaoLista.index(termo)==0:
                    if termo !='(' and termo in self.__prioridadesOperadoresChaves: # caso a operação apressente um operador no inicio. 
                        raise NotacaoException(f'o seguinte operador: "{termo}" foi inserido no inicio da operacao.')
                
                elif termo != '(' and termoAnterior !=')':
                    if  termo in self.__prioridadesOperadoresChaves and termoAnterior in self.__prioridadesOperadoresChaves: #caso seja recebida um operador após um outro operador.
                        raise NotacaoException(f'o seguinte operador: "{termo}" foi inserido logo após o operador: "{termoAnterior}".')
                
                termoAnterior=termo  

        except AssertionError as AE:
            raise NotacaoException(AE)
        else:
            self.conferirTermos(operacaoLista)
    

    def conferirTermos(self, listaTermos:list[str]):
        #Este método é responsável por coordenar os termos recebidos, se for uma letra: ela será entregue a saída, se um operador, será feito uma checagem.
        
        for valor in listaTermos:
            
            if valor in self.__prioridadesOperadoresChaves:
                self.conferirOperadorTipo(valor)
            else:
                self.__saida+=valor
        
        self.descarregarPilhaOperadores() # logo após destinar as letras para a saida e os operadores para a logica da pilha, o programa deverá descarregar todos os operadores restantes na pilha para a saida
    

    def conferirOperadorTipo(self, operador:str): #Este método é o mais importante, ele checará e dizerá se o operador entrará na pilha, 
        if len(self.__operacaoPilha)==0: # a pilha está vazia, então o operador pode ser inserido normalmente na pilha.
            self.empilharOperadorLista(operador)
        
        elif operador=='(':
            self.empilharOperadorLista(operador)

        elif operador== ')': #caso o operador seja um  ')' a pilha desempilhará até achar um '('
                parentesesAbertoAchado= True
                while parentesesAbertoAchado: 
                    parentesesAbertoAchado=self.desempilharOperadorLista() 
                      
        elif self.conferirOperadorMaiorIgualQueTopoPrioridade(operador): # caso o operador seja de prioridade menor que o anterior
            self.empilharOperadorLista(operador)
        
        else: 
            self.desempilharOperadorLista()
            self.empilharOperadorLista(operador)
    
    
    
    def conferirOperadorMaiorIgualQueTopoPrioridade(self,operador)->bool: #checa se a prioridade do operador no topo é maior que o operador analisado
        if self.__prioridadeTopo >= self.__prioridadesOperadores[operador]: # se a prioridade do topo for maior que o analisado
            return False
        else:
            return True
    
    def empilharOperadorLista(self, operador): #acrescenta um elemento no topo da pilha
        self.__operacaoPilha.append(operador)
        self.ArmazenarPrioridadeTopo(operador)
    
    
    def descarregarPilhaOperadores(self):
        while self.__operacaoPilha.__len__()>0:
            self.desempilharOperadorLista()

    def desempilharOperadorLista(self) ->boolean: #remove o elemento no topo da pilha
        operadorDesempilhado=self.__operacaoPilha.pop() 
        
        if operadorDesempilhado!='(': #caso o elemento desempilhado sej um '('
            self.__saida += operadorDesempilhado 
            return False
        
        if len(self.__operacaoPilha)>0: # Muda a pioridade do topo para o proximo elemento
            self.ArmazenarPrioridadeTopo(self.__operacaoPilha[len(self.__operacaoPilha)-1])
        return True
    

    def ArmazenarPrioridadeTopo(self,operador): #Armazena a prioridade do topo atual
        self.__prioridadeTopo= self.__prioridadesOperadores[operador]


    def mostrarSaida(self)->str: #retorna a Saida 
        return f'{self.__saida}'
    

    def mostrarOperadoresPilha(self)->str: #retorna a Pilha de operadores
        return f'{self.__operacaoPilha}'