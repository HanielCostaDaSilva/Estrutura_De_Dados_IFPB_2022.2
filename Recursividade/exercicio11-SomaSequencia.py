#a Sequencia é a seguinte: 1 1/2 1/3 1/4 1/5 1/6

def SomarTermosSequencia(TermoFinal):
    if TermoFinal<=1 :
        return 1

    soma=1/(TermoFinal)
    
    soma+=SomarTermosSequencia(TermoFinal - 1)
    
    return soma

n=int(input('Digite até qual termo deseja somar: '))

print('A soma dos termos até o termo final é de: ', SomarTermosSequencia(n))