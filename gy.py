import numpy as np

m = np.empty((2,2),dtype=float)
cont = 0

for linhas in range(2):
    for colunas in range(2):
        num = float(input('Digite um número: '))
        m[linhas][colunas] = num
        if m[linhas][colunas] == 0:
            cont == cont + 1 
            
            listam = []
            
            if m[linhas][colunas] > 5:
                listam.append(m[linhas][colunas])
                
        
print(m)
print(cont)