from notacaoPolonesa import *


N1=NotacaoPosfixa()
try:
    N1.receberOperacao(input())

except NotacaoException as NE:
    print(NE)
print(N1.mostrarOperadoresPilha())
print(N1.mostrarSaida())