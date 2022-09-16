class Farol:
    def __init__(self, cor:str, estado=False):
        self.__corFarol= cor
        self.estado=estado # o farol por padrão estará apagado, caso receba True, ele acenderá.  
        
    def mudarEstado(self): #O Próprio farol irá mudar o seu estado
        self.estado= not(self.estado) # se estiver True, ele se tornará False e assim por diante.
    
    def __str__(self):
        if self.estado==True: 
            situacao= 'ativo'
        else:
            situacao='apagado'
        return f'cor: {self.corFarol} estado: {situacao}'
    
    @property
    def corFarol(self):
        return self.__corFarol