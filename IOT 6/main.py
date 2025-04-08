import serial
import time
from banco import Banco

PORTA = "COM3"
ARDUINO = serial.Serial(PORTA, 9600, timeout=1)
time.sleep(2)

aluno = "Rodrigo"
led = 1
banco = Banco()
banco.criar_tabela()  # Corrigido: chamar a função com parênteses

while True:
    comando = input("Digite 1 para ligar o led e 0 para desligar o led: ")
    
    match comando:
        
        case "1":
            # ARDUINO.write(b'1')
            estado = "ligado"
            banco.inserir_ou_atualizar_estado(aluno, led, estado)
            print("'1' LED ligado")
        
        case "2":
            banco.listar_estados()
        case "0":
            estado = "desligado"
            # ARDUINO.write(b'0')
            banco.inserir_ou_atualizar_estado(aluno, led, estado)
            print("O LED está desligado")
        
        case "sair":
            print("Encerrando programa")
            ARDUINO.close()
            break
