import random

while True:
    print("-" * 50, "¡BIENVENIDO AL JUEGO: ADIVINA EL NÚMERO!",
          "La PC pensará un número entre 1 y 100.", "-" * 50, sep='\n')

    while True:
        try:
            limite = int(input("¿Cuántos intentos querés tener? (mínimo 1): "))
            if limite <= 0:
                print("El número debe ser mayor a 0. Intentá de nuevo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresá un número entero válido.")

    print("¡Perfecto! Tenés", limite, "intentos.")
    print("¡Empecemos!", "-" * 50, sep='\n')

    numero_secreto = random.randint(1, 100)
    intentos = 1

    while intentos <= limite:
        try:
            print("Intento", intentos, "/", limite)
            adivinanza = int(input("Ingresá un número (1-100): "))

            if not 1 <= adivinanza <= 100:
                print("¡Fuera de rango! Debe ser entre 1 y 100.")
                continue

            if adivinanza < numero_secreto:
                print("¡Más alto!")
            elif adivinanza > numero_secreto:
                print("¡Más bajo!")
            else:
                print("-" * 50, "¡FELICITACIONES!", sep='\n')
                print("¡Adivinaste en", intentos, "intentos!")
                print("-" * 50)
                jugar_otra = input("¿Querés jugar otra vez? (s/n): ").lower()
                if jugar_otra == "s":
                    break
                else:
                    print("¡Gracias por jugar! ¡Hasta la próxima!")
                    exit()

            intentos += 1

            if intentos > limite:
                print("-" * 50, "¡Se acabaron los intentos!",
                      "El número era:", numero_secreto, "-" * 50, sep='\n')
                jugar_otra = input("¿Querés jugar otra vez? (s/n): ").lower()
                if jugar_otra == "s":
                    break
                else:
                    print("¡Gracias por jugar! ¡Hasta la próxima!")
                    exit()

        except ValueError:
            print("Por favor, ingresá un número entero válido.")

