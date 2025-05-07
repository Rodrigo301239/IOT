import mysql.connector

class Banco:
    
    def __init__(self) -> None:
        self.__conexao = self.conectar ()
        self.__cursor = self.__conexao.cursor ()

    def conectar(self):
        return mysql.connector.connect(
            host = "paparella.com.br",
            user = "paparell_aluno_7",
            password = "@Senai2025",
            database = "paparell_python"
        )
    
    def criar_tabela(self):
        query = """
                 create table if not exists dispositivos(
                 id int auto_increment primary key,
                 aluno varchar(255) not null,
                 dispositivo varchar(255) not null,
                 valor int not null)
                 """
        self.__cursor.execute(query)
        self.__conexao.commit()

    def inserir_atualizar(self, aluno, dispositivo, valor):
        # verificar se o aluno
        query = "select id from dispositivos where aluno=%s"
        self.__cursor.execute(query,(aluno,))
        id = self.__cursor.fetchone() 
        if id:
            # atualizar dados
            query = "update dispositivos set dispositivo = %s, valor = %s where id = %s"
            self.__cursor.execute(query,(dispositivo,valor,id[0]))
            # print(f"Valor: {valor} cm do DISP: {dispositivo} do Aluno: {aluno}, atualizado com Sucesso")
            self.__conexao.commit()
        else:
            query = "insert into dispositivos(aluno,dispositivo,valor) values(%s,%s,%s)"
            self.__cursor.execute(query,(aluno,dispositivo,valor))
            # print(f"Valor: {valor} cm do DISP: {dispositivo} do Aluno: {aluno}, criado com Sucesso")
            self.__conexao.commit()

    def listar(self):
        query ="SELECT * FROM dispositivos"
        self.__cursor.execute(query)
        disp = self.__cursor.fetchall()
        if not disp:
            print("Dispositivos não encontrados")
        else:
            for d in disp:
                print(f"ID: {d[0]} | Aluno: {d[1]} | Dispositivo: {d[2]} | valor: {d[3]}")
        self.__conexao.commit()
        
    def fechar_conexao (self):
        if self.__conexao and self.__cursor:
            self.__conexao.close ()
            self.__cursor.close ()