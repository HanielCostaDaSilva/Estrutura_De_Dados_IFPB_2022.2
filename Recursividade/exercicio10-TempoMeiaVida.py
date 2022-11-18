def TempoDeMeiaVida(massa,tempoDeDecaimento)->list:
    
    if massa<=0.8:
        return [massa,0,0]
    resultado=TempoDeMeiaVida(massa/2,tempoDeDecaimento)
    resultado[1] +=1
    resultado[2]=resultado[1]*tempoDeDecaimento
    return resultado

massa=float(input('digite o valor da massa do elemento (g): '))
TempoDeDecaimento=float(input('digite o tempo que leva para o deicamento (s): '))

resultadoFinal=TempoDeMeiaVida(massa,TempoDeDecaimento)

print(f'o elemento de massa: {massa}, levou em torno de {resultadoFinal[2]} segundos, para sua massa decair para {resultadoFinal[0]} gramas. Ele decaiu {resultadoFinal[1]} vezes.')