from Paciente import Paciente
from Hospital import Hospital
from filaEncadeadaNoCabeca import Fila, FilaException
import time

class MedicException(Exception):
    def __init__(self,msg) -> None:
        super().__init__(f'MEDIC EXCEPTION: {msg}')

class Medico:
    
    '''
    #== == == == O médico deverá conter:
    #Nome= String sem restrição {O nome do médico em questão}
    
    #Especialidade= String, só pode ser uma especialidade cadastrada anteriormente na classe Hospital {
        Ela é responsável por ditar com qual Paciente o médico deverá interagir{
            EX: Paciente que busca um Oftamologísta, deve ser atendido por um médico com especialidade em Oftalmologia             
        }
        Não Deverá ser permitido um médico com uma especialidade que não esteja cadastra no hospital.  
        O médico só poderá conte uma única especialidade
    }
    
    #limiteMinutosConsultasSeguidas= Int, só pode ser aceito, limites de 30 minutos até 2hr e 30, ou seja, 150 minutos {
        Deverá ser consultada sempre quando o Hospital for marcar a consulta de um Paciente com um Médico
        Ela é  a responsável por permitir se um paciente poderá entrar ou não na lista de espera do médico{
            EX: Um médico que possui o limite de 70 minutos, e possui 69 minutos ocupado, ele deverá permitir que um paciente com valor X de tempo entre na fila, mas não poderá permitir que um outro paciente entre.
        }         
    }
    '''
        
    '''
    #== == == == O médico deverá Fazer:
    #Ele Poderá alterar seus atributos quando quiser desde que as modificações estejam de acordo com as restrições dos atributos.
    
    #Caso não tenha nenhum paciente para ser atendido, na sua fila de espera, o médico deverá ficar esperando a chegada de um paciente
    
    #Caso haja um paciente, o médico deverá atendê-lo, seguindo o tempo de consulta do paciente (divida o tempo de consulta do paciente por 10, para mais rapidez na aplicação)   
    '''
    
    def __init__(self, nome:str,especialidade:str, limiteMinutosConsultasSeguidas:int) -> None:
        
        assert limiteMinutosConsultasSeguidas >= 30 and limiteMinutosConsultasSeguidas<=150 , MedicException('INVALID TIME FOR A EXAM')
        self.__nome=nome
        self.__especialidade=especialidade
        self.__limiteMinutosConsultasSeguidas=limiteMinutosConsultasSeguidas
        #self.filaEspera= Fila() #-- -- Não sei se coloco aqui ou em Hospital
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    #== == == Só insere se a especialidade estiver na lista de especialidades do hospital
    def especialidade(self,especialidade):
        assert especialidade in Hospital.especialidadesLista, MedicException('SPECIALTY NOT REGISTERED IN HOSPITAL')
        self.__especialidade=especialidade
    
    @property
    def limiteMinutosConsultasSeguidas(self):
        return self.__tempoEstimadoConsultaMinutos

    @limiteMinutosConsultasSeguidas.setter
    def limiteMinutosConsultasSeguidas(self,tempoEstimado:int):
        try:
            assert tempoEstimado>=1 and type(tempoEstimado)==int
            self.__limiteMinutosConsultasSeguidas=tempoEstimado
        except AssertionError:
            raise MedicException('INVALID ENTERED TIME')


    def __str__(self) -> str:
        return f'Nome: {self.__nome}, Especialidade: {self.__especialidade}, Limite de tempo sequencial das consultas em minutos: {self.__limiteMinutosConsultasSeguidas}'
    
    def AtenderPaciente(self,paciente:Paciente): #== == ==O médico deverá atender o paciente que contém a sua especialidade

        TempoConsulta = paciente.__tempoEstimadoConsultaMinutos//10
        print( f'O paciente:{paciente.nome}, acabou de entrar no consultório do médico: {self.__nome}, especialidade: {self.__especialidade}')
        time.sleep(TempoConsulta) # momento do atendimento
        print( f'A consulta do paciente:{paciente.nome}, com o médico: {self.__nome}, especialidade: {self.__especialidade}, acabou!')
             
    def EsperarPacientes(self): #== == == O médico ficará esperando receber um paciente
        pass
    
    def __str__(self) -> str:
        return f'Nome: {self.__nome}, especialidade: {self.__especialidade}, Tempo Limite para consulta: {self.__limiteMinutosConsultasSeguidas}'