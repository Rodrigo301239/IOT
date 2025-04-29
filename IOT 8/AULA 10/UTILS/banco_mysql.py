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
        query = """
                 create table if not exists dispositivos(
                 id int auto_increment primary key,
                 aluno varchar(255) not null,
                 dispositivo varchar(255) not null,
                 valor int not null)
                 """
        cursor.execute(query)
        conexao.commit()
        cursor.close()
        conexao.close()

    def inserir_atualizar(self, aluno, dispositivo, valor):
        conexao = self.conectar()
        cursor = conexao.cursor()
        # verificar se o aluno
        query = "select id from dispositivos where aluno=%s"
        cursor.execute(query,(aluno,))
        id = cursor.fetchone() 
        if id:
            # atualizar dados
            query = "update dispositivos set dispositivo = %s, valor = %s where id = %s"
            cursor.execute(query,(dispositivo,valor,id[0]))
            print(f"Valor: {valor} cm do DISP: {dispositivo} do Aluno: {aluno}, atualizado com Sucesso")
            conexao.commit()
        else:
            query = "insert into dispositivos(aluno,dispositivo,valor) values(%s,%s,%s)"
            cursor.execute(query,(aluno,dispositivo,valor))
            print(f"Valor: {valor} cm do DISP: {dispositivo} do Aluno: {aluno}, criado com Sucesso")
            conexao.commit()
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = self.conectar()
        cursor = conexao.cursor()
        query ="SELECT * FROM dispositivos"
        cursor.execute(query)
        disp = cursor.fetchall()
        if not disp:
            print("Dispositivos não encontrados")
        else:
            for d in disp:
                print(f"ID: {d[0]} | Aluno: {d[1]} | Dispositivo: {d[2]} | valor: {d[3]}")
        conexao.commit()
        cursor.close()
        conexao.close()