def memoria():
    import random
    secuencia = ''
    for x in range(9):
        secuencia += str(random.randint(0,9))
    print(secuencia)
    input('Presiona Enter cuando estés listo ')
    print('\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ')
    usuario = input('Escribe la secuencia:')
    if usuario == secuencia:
        print('¡Has ganado!')
    else:
        print('¡Perdiste! La secuencia era', secuencia)
memoria()