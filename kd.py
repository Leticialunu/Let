linhas = int(input('Digite as linhas: '))
colunas = int(input('Digite as colunas: '))

import numpy as np


matriz = np.zeros((2,2) ,dtype=float)
for i in range(linhas):
    for j in range(colunas):
        valor = int(input('Digite o valor para o elemento [(i)][(j)]: '))
        matriz[i][j] = valor


for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] == 8:
            print('Esta dentro')
            
print(matriz)
        
              




