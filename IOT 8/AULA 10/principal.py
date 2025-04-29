from arduino_serial import Arduino
from banco_mysql import Banco
import time

PORTA = "COM5"
BAUDRATE = 9600
INTERVALO = 1.0

def principal():
    arduino = Arduino(port = PORTA, baudrate = BAUDRATE)
    arduino.conexao_aberta()
    bd = Banco()
    bd.criar_tabela()

    print("Iniciando leitura labial")
    try:
        while True:
            arduino.enviar("REQ\n")
            
            resposta = arduino.receber()
            
            print (f"Distancia: {resposta} cm")
            
            bd.inserir_atualizar("rodrigo", 1, resposta)
            
            bd.listar()
            
            time.sleep(INTERVALO)
    except KeyboardInterrupt:
        print("/nPrograma interrompido pelo usuario")
    except Exception as e:
        print (f"ERRO: {e}")
    finally:
        arduino.conexao_fechada()
        print("Conexao fechada")
        
    
if __name__ == "__main__":
    principal()