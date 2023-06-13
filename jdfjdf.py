lista = []

for elemento in range(4):
    n = float(input('Digite a nota: '))
    lista.append(n)
    
soma = sum(lista)
media = soma / 4
print('A média do aluno é: ', media)
