class PacientException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(f'PACIENT EXCEPTION: {msg}')


class Paciente:
    def __init__(self, nome:str,especialista:str, tempoEstimadoConsultaMinutos:int) -> None:
        self.__nome=nome
        self.__especialista=especialista
        self.__tempoEstimadoConsultaMinutos=tempoEstimadoConsultaMinutos
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def especialista(self):
        return self.__especialista
    
    @especialista.setter
    def especialista(self,especialista):
        self.__especialista=especialista
    
    @property
    def tempoEstimadoConsultaMinutos(self):
        return self.__tempoEstimadoConsultaMinutos

    @tempoEstimadoConsultaMinutos.setter
    def nome(self,tempoEstimado:int):
        try:
            assert tempoEstimado>0 and type(tempoEstimado)==int
            self.__tempoEstimadoConsultaMinutos=tempoEstimado

        except AssertionError:
            raise PacientException('INVALID ENTERED TIME')
             
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialista desejado: {self.__especialista}, tempo estimadoda consulta em minutos: {self.__tempoEstimadoConsultaMinutos}'
    