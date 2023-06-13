def investigacao():
    lista_resposta = []
    print('Digite somente s ou n')
    
    perg1 = (input('Telefonou para a vitima? '))
    lista_resposta.append(perg1)
    perg2 = (input)('Esteve no local do crime? ')
    lista_resposta.append(perg2)
    perg3 = (input('Mora perto da vítima? '))
    lista_resposta.append(perg3)
    perg4 = (input('Devia para a vítima? '))
    lista_resposta.append(perg4)
    perg5 = (input('Ja trabalhou com a vitima? '))
    lista_resposta.append(perg5)
    

    qtdsim = lista_resposta.count('s')
    
    if qtdsim == 2:
        print('Suspeito.')
    elif qtdsim == 3 or qtdsim == 4:
        print('Cúmplice.')
    elif qtdsim == 5:
        print('Assassino!!!')
    else:
        print('Inocente')
        
investigacao()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
