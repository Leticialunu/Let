import numpy as np

matriz_vazia = np.empty((2, 2))
cont = 0

for i in range(2):
    for j in range(2):
        valor = int(input('Digite o valor do elemento: '))
        matriz_vazia[i][j] = valor
        if matriz_vazia [i][j] == 0:
            cont = cont + 1
           
            
        
print(matriz_vazia)
print(cont)
