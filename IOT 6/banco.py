import mysql.connector

class Banco:

    def conectar(self):
        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_8",
            password = "@Senai2025",
            database = "paparell_python"
        )
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        query = ("""
                 create table if not exists leds(
                 id int auto_increment primary key,
                 aluno varchar(255) not null,
                 led int not null,
                 estado varchar(255) not null)
                 """)
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()

    def inserir_ou_atualizar_estado(self,aluno,led, estado):
        conexao = self.conectar()
        cursor = conexao.cursor()
        # verificar se o aluno
        query = "select id from leds where aluno=%s"
        cursor.execute(query,(aluno,))
        id = cursor.fetchone() 
        if id:
            # atualizar dados
            query = "update leds set estado = %s where id = %s"
            cursor.execute(query,(estado,id[0]))
            print(f"Estado do LED do Aluno: {aluno}, atualizado com Sucesso")
        else:
            query = "insert into leds(aluno,led,estado) values(%s,%s,%s)"
            cursor.execute(query,(aluno,led,estado))
            print(f"Estado do LED do Aluno: {aluno}, criado com Sucesso")
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def listar_estados(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        
        query = "select * from leds"
        cursor.execute(query)
        leds = cursor.fetchall()
        
        if not leds:
            print ("erro")
        else:
            for led in leds:
                print(f"ID: {led[0]} | Aluno: {led[1]} | Led {led[2]} | Estado {led[3]}")
            conexao.commit()
            cursor.close()
            conexao.close()
            
    def ler_estado (self,aluno):
        conexao = self.conectar()
        cursor = conexao.cursor()
        
        query = "SELECT estado FROM leds WHERE aluno = %s"
        cursor.execute(query,(aluno,))
        estado = cursor.fetchone
        return estado[0]
            