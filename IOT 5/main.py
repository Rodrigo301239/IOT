from empresa import Funcionario

def main():
    funcionario = Funcionario()
    funcionario.criar_tabela()
    while True:
        print("\n")
        print("[1] adicionar funcionario")
        print("[2] listar Funcionarios")
        print("[3] atualizar salari")
        print("[4] excluir funcionario")
        print("[5] sair do programa")
        print("[6] alterar cargo")
        print("[7] alterar departamento")
        
        
        opcao = int(input("digite: "))
        
        match opcao:
            case 1:
                funcionario.adicionar_funcionario()
            case 2:
                funcionario.listar_funcionarios()
            case 3:
                funcionario.atualizar_salario()
            case 4:
                funcionario.excluir_funcionario()
            case 5:
                break
            case 6:
                funcionario.alterar_cargo()
            case 7:
                funcionario.alterar_departamento()
    
            
            case _:
                print("Opcao invalida")

if __name__ == "__main__":
    main()