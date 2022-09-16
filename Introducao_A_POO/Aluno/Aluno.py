
import string


class Aluno:
    
    def __init__(self,matricula:int,nome:string, notas:list) -> None:
        self.__notas=notas
        self.__nome= nome
        self.__matricula=matricula
    
    @property
    def nome(self) ->string:
        return self.__nome
    
    @property
    def notas(self) ->string:
        return self.__notas
    
    @property
    def matricula(self)->string:
        return string(self.__matricula) 
    
    def CalcularMedia(self):
        soma=0
        for i in range(len(self.__notas)):
            soma +=self.notas[i]
        return soma/self.__notas.__len__()
    
    @nome.setter
    def setNome(self,novoNome:string):
        self.__nome=novoNome
    
    def AdicionarNota(self,novaNota:float,posicao=-1):
        self.__notas.insert(posicao,novaNota)
    
    def MostrarNotas(self):
        return ' '.join(self.__notas)
    
    def __str__(self) -> str:
        return f'Matrícula: {self.__matricula} \n nome: {self.__nome} \n notas: {self.__notas}'
    
    