def juego_del_dado():
    """
    Esta función tiene que pedirle al usuario que aprete enter para que lance un dado.
    Esto genera un número al azar que se le suma a la puntuación del usuario.
    Después el computador también tiene que lanzar un dado.
    El primero en sumar 30 puntos gana.
    """
    import random
    contador_usuario = 0
    contador_computador = 0
    while contador_usuario < 30 and contador_computador < 30:
        adelante = input("Tira el dado ")
        numero_usuario = random.randint(1,6)
        print("Tu numero es:",numero_usuario)
        contador_usuario += numero_usuario
        if contador_usuario < 30:
            numero_computador = random.randint(1,6)
            print("El numero del computador es:",numero_computador)
            contador_computador += numero_computador
        else:
            print("Le ganaste al computador! Llegaste a 30 puntos")
    if contador_computador >= 30:
        print("Fuiste derrotado por el computador")

juego_del_dado()