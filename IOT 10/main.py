import socket
import time

HOST = ["192.168.1.177","192.168.1.178", "192.168.1.105"]
PORT =  5000

MAX_TENTATIVAS = 30
TIMEOUT = 5

while True:
        ip = int(input("Escolhe 1 para Arduino 1 ou 3 para Arduino 2: "))
        opcao = input("escolha 1 para ligar ou 0 para desligar: ")
        
        if ip > 3 :
             print("Dispositivo Invalido! Programa Encerrado")
             break
        elif opcao == "1":
            msg = b"ligar\n"
        elif opcao == "0":
            msg = b"desligar\n"
        else:
             print("Opção Invalida! Programa Encerrado")
             break
        
        s= None
        for tentativa in range(1, MAX_TENTATIVAS + 1):
            try:
                print(f"Tentando abrir conexão com ip: {HOST[ip-1]}")
                s = socket.create_connection((HOST[ip-1], PORT), timeout=2)
                print("Conexão aberta")
                s.settimeout(TIMEOUT)
                s.sendall(msg)         # ou b"ligar\n"
                print(f"Comando executado: {s.recv(16).decode()}")
                break
            except socket.timeout:
                print(f"Tempo esgotado (tentativa {tentativa}/{MAX_TENTATIVAS}).")
            except OSError as e:
                print(f"Falha de rede ({e}) (tentativa {tentativa}/{MAX_TENTATIVAS}).")

            finally:
                if s:                    # fecha só se o socket existe
                    s.close()
                    print("Conexão fechada.\n")