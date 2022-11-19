class PacientException(Exception):
    def __init__(self, msg) -> None:
        super().__init__(f'PACIENT EXCEPTION: {msg}')


class Paciente:
    '''
    #== == == == O Paciente deverá conter:
    #Nome= String sem restrição {O nome do Paciente em questão}
    
    #EspecialistaDesejado= String, sem restrição{
        Ela é responsável por ditar com qual  Médico o Paciente deverá interagir{
            EX: Paciente que busca um Oftamologísta, deve ser atendido por um Medico com especialidade em Oftalmologia             
        }
        O paciente pode desejar qualquer tipo de especialidade, mas o Hospital só poderá admitir uma consulta com  um Médico que contenha a tal especialidade.  
        O Paciente só poderá desejar a consulta com um único especialista.
    }
    
    #tempoEstimadoConsultaMinutos= Int, só pode ser aceito, consultas de 1 minuto ou acima{
            Ela é  a responsável por permitir que  um paciente  entrar ou não na lista de espera do Médico{
            EX: Um Paciente que possui uma consulta de 70 minutos, e o médico só possui  1 minuto livre, o paciente poderá entrar na fila, pois o limite ainda não foi atingido.
        }         
    }
    '''
        
    '''
    #== == == == O Paciente deverá Fazer:
    #Ele Poderá alterar seus atributos quando quiser desde que as modificações estejam de acordo com as restrições dos atributos.
    '''
    
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
    def tempoEstimadoConsultaMinutos(self,tempoEstimado:int):
        try:
            assert tempoEstimado>0 and type(tempoEstimado)==int
            self.__tempoEstimadoConsultaMinutos=tempoEstimado

        except AssertionError:
            raise PacientException('INVALID ENTERED TIME')
             
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialista desejado: {self.__especialista}, tempo estimadoda consulta em minutos: {self.__tempoEstimadoConsultaMinutos}'
    