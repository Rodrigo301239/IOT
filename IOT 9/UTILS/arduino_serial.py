import time
import serial

class Arduino:
    
    def __init__ (self, port, baudrate, timeout = 1.0, resset_delay = 2.0):
        self.__port = port
        self.__baudrate = baudrate
        self.__timeout = timeout
        self.__rest_delay = resset_delay
        
        self.__ser = None
    
    def conexao_aberta (self):
        self.__ser = serial.Serial (
            port = self.__port,
            baudrate = self.__baudrate,
            timeout = self.__timeout
        )
        time.sleep (self.__rest_delay)
        
        
    def conexao_fechada (self):
        if self.__ser and self.__ser.is_open:
            self.__ser.close ()
            
    def enviar (self, dados):
        if not (self.__ser and self.__ser.is_open):
            raise serial.SerialException ("Porta Serial não está Aberta!")
        self.__ser.write (dados.encode ("utf-8"))
        self.__ser.flush ()
        
    def receber (self):
        if not (self.__ser and self.__ser.is_open):
            raise serial.SerialException ("Porta Serial não está Aberta")
        dado = self.__ser.readline ()
        return dado.decode ("utf-8").strip ("\r\n")