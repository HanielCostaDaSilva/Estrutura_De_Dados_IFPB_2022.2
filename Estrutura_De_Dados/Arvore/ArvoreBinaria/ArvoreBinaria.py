#== == == == Onde os elementos da árvore são criados
class No:
    def __init__(self, carga:any):
        self.carga = carga
        self.esq = None
        self.dir = None

    def __str__(self):
        return f'{self.carga}'
    
class Arvore:
    def __init__(self,valorInicial) -> None:
        self.__raiz= No(valorInicial)