def adivinar_par_o_impar():
    """
    Esta función representa el juego de adivinar si un número es par o impar.
    Tienes que permitir que el usuario ingrese una de las dos opciones y
    generar un número aleatorio para ver si es par o impar.
    Se debe mostrar si el usuario adivina correctamente o no.
    """
    import random
    par_o_impar = input("Adivina si es par o impar: ")
    numero = int(random.randint(1,101))
    if numero%2 == 0:
        numero = "par"
    else:
        numero = "impar"
    if par_o_impar == numero:
        print("Correcto! El número era "+numero)
    else:
        print("Incorrecto, el número era "+numero)
adivinar_par_o_impar()