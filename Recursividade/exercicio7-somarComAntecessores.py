def somarComAntecessores(numero):
    if numero==0:
        return numero
    #print(numero)
    return numero + somarComAntecessores(numero-1)

numero=int(input('digite um numero: '))
print(somarComAntecessores(numero))