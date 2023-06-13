funcionarios = {}
def cadastro():
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


def exibir_func():
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
        
cadastro()

def exibir_funcionarios():
    if funcionarios:
        print('Lista de funcionários: ')
        for nome, funcinario in funcionarios.items():
             
            print('Nome:', funcionario['nome'])
            print('Idade',funcionario['idade'])
            print('Cargo',funcionario['cargo'])
            print('salario',funcionario['salario'])
            
    else:
        print('Não há funcionários cadastrados.')
        
