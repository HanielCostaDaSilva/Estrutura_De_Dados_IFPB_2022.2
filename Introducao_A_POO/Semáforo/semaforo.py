import time
from typing import List

class Semaforo :

    
    def __init__(self, tempoParaMudarCor=10, *farois):    
        self.__tempoParaMudarCor=tempoParaMudarCor
        self.__caixaDeFarois=self.definirStatusInicial(farois)
        self.farolAtivo= self.definirFarolAtivo()
 

    def definirStatusInicial(self,farois:list)-> list: #Função usada para definir qual os farois que ficaria ligado  no semaforo
        farolLigado=False
        for i in range(len(farois)):
            if farois[i].estado == True and farolLigado == False: #Foi encontrado o primeiro farol ligado 
                farolLigado=True
            elif farois[i].estado == True and farolLigado == True: #Foi encontrado mais um farol ligado
                farois[i].mudarEstado() #'Desliga' o farol
        
        if farolLigado == False: #Não achou faróis ligados 
            farois[0].mudarEstado()
        
        return farois
    
    def MostrarStatus(self): # serve para mostrar as cores e estado dos farois
        for i in range(len(self.__caixaDeFarois) ) :
            if self.__caixaDeFarois[i].estado == True: #O farol está acesso
                situacao="X"
            else: 
                situacao=" "
            #print(f"{'______':^50}")
            print(f"\n {self.__caixaDeFarois[i].corFarol : ^50}|  ( {situacao} )  |\n")
        print()
    
    def retornarInformacaoFarois(self)->List:
        caixaFarolLista=[]
        farolInformacaoLista=[]
        for i in range(len(self.__caixaDeFarois)):
            caixaFarolLista.append(self.__caixaDeFarois[i].__str__())
        return caixaFarolLista
                

    def definirFarolAtivo(self):
        for i in range(len(self.__caixaDeFarois)):
            if self.__caixaDeFarois[i].estado == True:
                return self.__caixaDeFarois[i]
    
    def temporizarParaMudarSemaforo(self):
        for i in range(self.__tempoParaMudarCor):
            print(f"Vou mudar de cor em {self.__tempoParaMudarCor - i} segundos")
            time.sleep(1)
        self.trocarFarolAtivo()
    
    def trocarFarolAtivo(self):
        if self.__caixaDeFarois.index(self.farolAtivo) == 0 : # caso seja o primeiro farol (de cima para baixo) o ativo, ele terá que ir para o último farol.
            self.farolAtivo.mudarEstado()
            self.farolAtivo= self.__caixaDeFarois[len(self.__caixaDeFarois)-1]
            self.farolAtivo.mudarEstado()
        else: # Caso seja o ultimo(de cima para baixo) ou outro farol sem ser o primeiro 
            self.farolAtivo.mudarEstado()
            self.farolAtivo= self.__caixaDeFarois[self.__caixaDeFarois.index(self.farolAtivo)-1]
            self.farolAtivo.mudarEstado()
            
    
    def __str__(self):
        return f"Farois: {self.retornarInformacaoFarois()} tempo para mudar entre farois: {self.__tempoParaMudarCor}."