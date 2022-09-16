class PilhaException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class No :
    def __init__(self,valor) -> None:
        self.value= valor
        self.prox= None
    
    def __str__(self):
        return 'Valor do nó: '+ self.value
    
    
class Pilha:
    def __init__(self):
        self.__start= None
        self.__tamanho=0

    def estaVazia(self)->bool:
        return self.__tamanho == 0

    @property
    def tamanho(self)->int:
        return self.__tamanho


    def elemento(self, posicao:int)->any:
        try:
            assert not self.estaVazia() ,'A lista está vazia!'
            assert self.__tamanho>=posicao and posicao>0, f'A posição inserida é inválida, pois o tamanho da pilha é de {self.__tamanho} nó(s)!'
            
            cursor=self.__start
            passos= self.__tamanho - posicao
            cont=1
            while cont < passos:
                
                
        except AssertionError as AE:
            raise PilhaException(AE)
    
    def busca(self, conteudo:any)->int:
        for i in range(len(self.__dados)):
            if self.__dados[i] == conteudo:
                return i+1
        raise  PilhaException(f'Valor {conteudo} não está na pilha')

    def modificar(self, posicao:int, conteudo: any):
        try:
            self.__dados[posicao-1] = conteudo
        except IndexError:
            raise PilhaException(f'Posicao inválida para a pilha atual com {len(self.__dados)} elementos')

    def empilha(self, conteudo:any):
        self.__dados.append(conteudo)

    def desempilha(self)->any:
        if self.estaVazia():
            raise PilhaException(f'Pilha vazia.')
        return self.__dados.pop()

    def __str__(self):
        s = ''
        for e in self.__dados:
            s+=f'{e} '
        return s

    def esvazia(self):
        self.__dados.clear()





