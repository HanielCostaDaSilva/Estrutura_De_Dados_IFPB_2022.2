from Paciente import Paciente
import time

class Medico:

    def __init__(self, nome:str,especialidade:str, limiteMinutosConsultasSeguidas:int) -> None:
        self.__nome=nome
        self.__especialidade=especialidade
        self.__limiteMinutosConsultasSeguidas=limiteMinutosConsultasSeguidas
    
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialidade: {self.__especialidade}, Limite de tempo sequencial das consultas em minutos: {self.__limiteMinutosConsultasSeguidas}'
    
    def AtenderProximo(self,paciente:Paciente): #o médico deverá atender o próximo paciente que contém a sua especialidade
        TempoConsulta = paciente.__tempoEstimadoConsultaMinutos//10

        print( f'O paciente:{paciente.nome}, acabou de entrar no consultório do médico: {self.__nome}, especialidade: {self.__especialidade}')
        time.sleep(TempoConsulta) # momento do atendimento
        print( f'A consulta do paciente:{paciente.nome}, com o médico: {self.__nome}, especialidade: {self.__especialidade}, acabou!')
             
    def EsperarPacientes(self): # O médico ficará esperando receber um paciente
        pass
    