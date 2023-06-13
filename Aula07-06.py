#Aula 07/06 - Continuação do código da biblioteca

funcionarios = {}
def cadastrar_funcionario():
    nome = input('Digite o nome do funcionário: ')
    idade = int(input('Digite a idade do funcionário: '))
    cargo = input('Digite o cargo do funcionário: ')
    salario = float(input('Digite o sálario do funcionário: '))
    
    funcionario = {
        "nome": nome,
        "idade": idade,
        "cargo": cargo,
        "salario": salario
    }    
    
    funcionarios[nome] = funcionario
    print('Funcionário cadastrado com sucesso!')


def exibir_funcionario():
    nome = input('Digite o nome dos funcionários: ')
    
    if nome in funcionarios:
        funcionario = funcionarios[nome]
        print('Dados do funcionários: ')
        print('Nome:', funcionario['nome'])
        print('Idade',funcionario['idade'])
        print('Cargo',funcionario['cargo'])
        print('salario',funcionario['salario'])
    else:
        print('Funcionário não encontrado.')


def exibir_funcionarios():
    if funcionarios:
        print('Lista de funcionários: ')
        for nome, funcionario in funcionarios.items():
             
            print('Nome:', funcionario['nome'])
            print('Idade',funcionario['idade'])
            print('Cargo',funcionario['cargo'])
            print('salario',funcionario['salario'])
            print("-"*30)
            
    else:
        print('Não há funcionários cadastrados.')
        
def remover_funcionario():
    nome = input("Digite o nome do funcionário: ")
    if nome in funcionarios[nome]:
        print("Funcionário removido com sucesso!")
    else:
        print("Funcionário não encontrado!")

while True:
    print("\n=== Sistema de cadastro de funcionários ===")
    print("1 - Cadastrar funcionário")
    print("2 - exibir dados de um funcionário")
    print("3 - exibir todos os funcionários cadastrados")
    print("4 - Remover funcionário")
    print("0 - Sair")
    
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        cadastrar_funcionario()
    elif opcao == "2":
        exibir_funcionario()
    elif opcao == "3":
        exibir_funcionarios()
    elif opcao == "4":
        remover_funcionario()
    elif opcao == "0":
        print("Sessão finalizada!")
        break
    else:
        print("Opção inválida! digite novamente.")
