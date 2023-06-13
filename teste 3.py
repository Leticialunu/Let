salario = float(input('Digite o salário: '))

if salario < 280:
    reajuste = salario * 0.2 
    salario_novo = reajuste + salario
    print('Salário antigo: ', salario)
    print('Salário novo: ', salario_novo)
    print('Percentual aplicaddo, 20%')
    print('O valor do aumento: ',reajuste)
    
if salario >= 280 and salario < 700:
    reajuste = salario * 0.15
    salario_novo = reajuste + salario
    print('Salário antigo, ',salario)
    print('Salário novo: ',salario_novo)
    print('Porcentual aplicado: 15%')
    print('O valor do aumento: ', reajuste)
    
if salario >= 700 and salario < 1500:
    reajuste = salario * 0.10 
    salario_novo = reajuste + salario
    print('Salário antigo, ',salario)
    print('Salário novo: ',salario_novo)
    print('Porcentual aplicado: 10%')
    print('O valor do aumento: ', reajuste)
    
if salario >= 1500: 
    reajuste = salario * 0.5
    salario_novo = reajuste + salario
    print('Salário antigo, ',salario)
    print('Salário novo: ',salario_novo)
    print('Porcentual aplicado: 5%')
    print('O valor do aumento: ', reajuste)
    
    


    


 