lista1 = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10]
lista2 = [8, 7, 5, 10, 9]

comuns = []

for elemento in lista1:
    if elemento in lista2:
        comuns.append(elemento)
        
print(comuns)
   