def piedra_papel_tijera():
    import random
    computadora = ''
    numero = random.randint(1,3)
    if numero == 1:
        computadora = 'piedra'
    elif numero == 2:
        computadora = 'papel'
    else:
        computadora = 'tijera'
    usuario = input('Elige piedra, papel o tijera: ')
    print('Tu:', usuario, '\nComputadora:', computadora)
    if usuario == computadora:
        print('¡Empate!')
        return
    if usuario == 'piedra':
        if computadora == 'papel':
            print('¡Perdiste!')
        elif computadora == 'tijera':
            print('¡Has ganado!')
    if usuario == 'tijera':
        if computadora == 'piedra':
            print('¡Perdiste!')
        elif computadora == 'papel':
            print('¡Has ganado!')
    if usuario == 'papel':
        if computadora == 'tijera':
            print('¡Perdiste!')
        elif computadora == 'piedra':
            print('¡Has ganado!')
piedra_papel_tijera()