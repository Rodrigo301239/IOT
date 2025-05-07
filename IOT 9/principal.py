from UTILS.arduino_serial import Arduino
from UTILS.banco_mysql import Banco
import time
import os
import threading

# CONFUGURAÇÃO
PORTA = "COM5"
BAUDRATE = 9600
INTERVALO = 1.0

#VARIAVEIS GLOBAIS
aluno = "Kawann"
resposta = ""
dispositivo = "Ultrassom"

# Evento para encerrar o programa
fechar_threads = threading.Event ()

def thread_arduino ():
    global resposta
    arduino = Arduino (port = PORTA, baudrate = BAUDRATE)
    arduino.conexao_aberta ()
    
    try:
        while not fechar_threads.is_set ():
            # Enviar requisição para Arduino
            arduino.enviar ("REQ\n")
            
            # Receber dados Arduino
            resposta = arduino.receber ()
            
            time.sleep (INTERVALO)
    except Exception as e:
        print (f"ERRO -> {e}")
    finally:
        arduino.conexao_fechada ()
        print ("Conexão com o Arduino Encerrada")
        
def thread_bd ():
    global aluno
    global resposta
    global dispositivo
    bd = Banco ()
    bd.criar_tabela ()
    
    try:
        while not fechar_threads.is_set ():
            bd.inserir_atualizar (aluno, dispositivo, resposta)
            time.sleep (INTERVALO)
    except Exception as e:
        print (f"ERRO -> {e}")
    finally:
        bd.fechar_conexao ()
        print ("Conexão do MySQL Encerrada")

def thread_menu ():
    global dispositivo
    global aluno
    leitura_bd = Banco ()
    
    try:
        while not fechar_threads.is_set ():
            os.system ("cls")
            print ("1 - Mudar Aluno")
            print ("2 - Atualizar ou Inserir")
            print ("3 - Lista Dispositivos")
            print ("4  - Sair")
            opcao = input ("Escolha uma Opção: ")
            
            match opcao:
                case "1":
                    aluno = input ("Escreva o Nome do  Aluno: ")
                    print (f"Nome do Aluno alterado para: {aluno}")
                    input ("Aperte o ENTER para continuar...")
                case "2":
                    dispositivo = input ("Escreva o Nome do Dispositivo: ")
                    print (f"Dispositivo alterado para: {dispositivo}")
                    input ("Aperte o ENTER para continuar...")
                case "3":
                    leitura_bd.listar ()
                    input ("Aperte o ENTER para continuar...")
                case "4":
                    fechar_threads.set ()
                case _:
                    print ("Opção Inválida... Tente Novamente")
                    input ("Aperte o ENTER para continuar...")
    except Exception as e:
        print (f"ERRO -> {e}")
    finally:
        leitura_bd.fechar_conexao ()
        print ("Conexão do MySQL Encerrada")

def principal ():
    ta = threading.Thread (target = thread_arduino)
    tbd = threading.Thread (target = thread_bd)
    tm = threading.Thread (target = thread_menu)
    ta.start ()
    tbd.start ()
    tm.start ()

if __name__ == "__main__":
    principal ()