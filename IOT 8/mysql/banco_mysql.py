import mysql.connector

class Banco:
    def conectar (self):
        return mysql.connector.connect (
        host = "paparella.com.br",
        user = "paparell_aluno_8",
        password = "@Senai2025",
        database = "paparell_python"   
            
        )
        
    
    def criar_tabela(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        
        query = ("create table if not exists dispositivos(id int auto_increment primary key, aluno varchar(255) not null, dispositivo int not null, valor decimal(10,2) not null)")
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()
        
    def inserir_atualizar(self, aluno, dispositivo, valor):
        conexao = self.conectar()
        cursor = conexao.cursor()
        
        query = "INSERT into dispositivos (aluno, dispositivo, valor) values (%s,%s,%s) on duplicate key update dispositivo = values (dispositivo), valor = (values(valor))"
        cursor.execute(query,(aluno,dispositivo,valor))
        print(((f"valor: {valor} inserido/atualizado com sucesso no dispositivo {dispositivo}")))
        cursor.close()
        conexao.close()
        
    def lista (self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query = "select * from dispositivos"
        cursor.execute(query)
        disp = cursor.fetchall()
        
        if not disp:
            print("dispositivo carbonizado")
        else:
            print(f"ID: {disp [0]} | Aluno {disp [1]} | Dispositivo: {disp [2]} | valor: {disp [3]}")
            cursor.close()
            conexao.close()
        
        