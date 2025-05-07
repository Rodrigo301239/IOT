import socket
import time
# byte mac1[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x03 }; RAFAEL 192.168.1.10
# byte mac2[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x04 }; DAYANE 192.168.1.11
# byte mac3[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x05 }; ERICK 192.168.1.12
# byte mac4[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x06 }; DIEMERSON 192.168.1.106
# byte mac5[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x07 }; KAUAN 192.168.1.105
# byte mac6[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x08 }; RODRIGO 192.168.1.174
# byte mac7[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x09 }; RIAN 192.168.1.167
# byte mac8[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x0A }; RAFAEL 192.168.1.157
# byte mac9[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0x0B }; DAVI 192.168.1.178
                                                
HOST = ["192.168.1.177",
        "192.168.1.178",
        "192.168.1.10",
        "192.168.1.11",
        "192.168.1.157",
        "192.168.1.167",
        "192.168.1.105",
        "192.168.1.174",
        "192.168.1.106",
        "192.168.1.178",
        "192.168.1.12"
        ]
PORT =  5000

MAX_TENTATIVAS = 30
TIMEOUT = 5

while True:
        ip = int(input("Escolhe  de 1 té 9 para Arduino: "))
        opcao = input("escolha 0 ou 1 para o LED, ou ultra para ultrassom: ")
        
        if ip > 11 :
             print("Dispositivo Invalido! Programa Encerrado")
             break
        elif opcao == "1":
            msg = b"ligar\n"
        elif opcao == "0":
            msg = b"desligar\n"
        elif opcao.lower() == "distancia":
            msg = b"distancia\n"
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