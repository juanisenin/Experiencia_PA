def adivinar_numero():
    import random
    numero = random.randint(1,10)
    intento = int(input('adivina el numero: '))
    if numero == intento:
        print('¡Has adivinado el número!')
    else:
        print('No has adivinado el número, el numero era:', str(numero), ':(')
adivinar_numero()
    