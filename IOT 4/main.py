from database import Pizza

def main():
    pizza = Pizza()
    pizza.adicionar_pizza("margarita","medias",35.00)
    pizza.listar_pizzas()

if __name__ == '__main__':
    main()