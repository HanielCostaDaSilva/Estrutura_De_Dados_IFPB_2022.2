from Farol import Farol
from semaforo import Semaforo
import time

Vermelho=Farol('Vermelho',True)
Amarelo=Farol('Amarelo',True)
Verde=Farol('Verde',True)
Azul=Farol('Azul',True)
Roxo=Farol('Roxo',True)
Laranja=Farol('Laranja',True)
Tempo_Para_Mudar_Semaforo=0
while Tempo_Para_Mudar_Semaforo<=0:
    try:
        Tempo_Para_Mudar_Semaforo=int(input("Qual o tempo desejado para alternar entre os faróis? "))
    except ValueError:
        print("Por favor! Digite apenas números inteiros!")
time.sleep(3)
Semaforo1=Semaforo(Tempo_Para_Mudar_Semaforo,Vermelho,Amarelo,Verde,Azul,Roxo,Laranja)

print(Semaforo1)

repetirVezes=0
while repetirVezes<=0:
    try:
        repetirVezes=int(input("Quantas vezes desejas repetir o sistema? "))
    except ValueError:
        print("Por favor! Digite apenas números inteiros!")
cont=1

while True:
    
    if repetirVezes<cont:
        resposta=input( f" Deseja repetir o experimento {repetirVezes} vezes, de novo (S/N)? ")
        while resposta.upper()!='S' and resposta.upper()!='N':
            resposta=input( f"(S ou N): ")
        if resposta.upper()=="S":
            cont=1
            continue
        else:
            break
    cont+=1
        
    Semaforo1.temporizarParaMudarSemaforo()
    Semaforo1.MostrarStatus()
    