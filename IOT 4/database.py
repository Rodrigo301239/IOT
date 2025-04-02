import mysql.connector

class Pizza:
    
    def __init__(self):
        self.__conexao = mysql.connector.connect(
            host = 'localhost',
            user = 'rodrigo',
            password = '1234',
            database = 'pizzaria'
        )
        self.__cursor = self.__conexao.cursor()
        self.criar_tabela()
        
    def criar_tabela(self):
        query =("""
                create table if not exists pizzas(
                    id int auto_increment primary key,
                    nome varchar(255) not null,
                    tamanho varchar(255)not null default 'grande',
                    preco decimal(10,2))
                    """)
        self.__cursor.execute(query)
        self.__conexao.commit()
        
    def adicionar_pizza(self,nome,tamanho,preco):
        self.__cursor.execute('insert into pizzas(nome,tamanho,preco) values (%s,%s,%s)',(nome, tamanho, preco))
        self.__conexao.commit()
        print("pizza adicionada com sucesso")
            
    def listar_pizzas(self):
        self.__cursor.execute("select * from pizzas")
        pizzas = self.__cursor.fetchall()
        #print (pizzas)
        if not pizzas:
            print ("pizzas nao cadastradas")
        else:
            for pizza in pizzas:
                print(f'ID: {pizza[0]} | Nome: {pizza[1]} | Tamanho {pizza[2]} | Preço: R$ {pizza[3]}')
        self.__conexao.commit()
    
    def excluir_pizzas (self):
        self.listar_pizzas()
        pizza_id = int(input("Digite o id da pizza: "))
        self.__cursor.execute("delete from pizzas where id = %s",(pizza_id,))
        self.__conexao.commit()
        print("pizza excluida com sucesso")
           
            