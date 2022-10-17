class Paciente:
    def __init__(self, nome:str,especialidade:str, limiteMinutosConsultasSeguidas:int) -> None:
        self.__nome=nome
        self.__especialidade=especialidade
        self.__limiteMinutosConsultasSeguidas=limiteMinutosConsultasSeguidas
    
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialidade: {self.__especialidade}, Limite de tempo sequencial das consultas em minutos: {self.__limiteMinutosConsultasSeguidas}'
    
    