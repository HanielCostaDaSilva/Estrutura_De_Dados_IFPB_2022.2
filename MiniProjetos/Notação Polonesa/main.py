from notacaoPolonesa import *


N1=NotacaoPosfixa()
try:
    while True:
        N1.receberOperacao(input('Digite uma operação: '))
        print(N1.mostrarSaida())
        
except NotacaoException as NE:
    print(NE)