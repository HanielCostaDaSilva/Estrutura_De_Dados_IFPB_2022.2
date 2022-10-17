class Paciente:
    def __init__(self, nome:str,especialista:str, tempoEstimadoConsultaMinutos:int) -> None:
        self.__nome=nome
        self.__especialista=especialista
        self.__tempoEstimadoConsultaMinutos=tempoEstimadoConsultaMinutos
    
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialista desejado: {self.__especialista}, tempo estimadoda consulta em minutos: {self.__tempoEstimadoConsultaMinutos}'
        