import random


palabras = ["paz", "amor", "casa", "gato", "perro", "libro", "juego"]

palabra = random.choice(palabras)
letras_adivinadas = set()
intentos_restantes = 6  
palabra_oculta = ["_"] * len(palabra)  

print("Bienvenido al ahorcado")

while intentos_restantes > 0 and "_" in palabra_oculta:
    print("\nPalabra:", " ".join(palabra_oculta))
    letra = input("Adivina una letra: ").lower()

    if letra in letras_adivinadas:
        print("Ya has probado esa letra, intenta otra.")
    elif letra in palabra:
        print("Correcto")
        letras_adivinadas.add(letra)
        for i, l in enumerate(palabra):
            if l == letra:
                palabra_oculta[i] = letra
    else:
        print("Incorrecto.")
        intentos_restantes -= 1
        letras_adivinadas.add(letra)
        print(f"Te quedan {intentos_restantes} intentos.")
if "_" not in palabra_oculta:
    print("\nFelicidades, ganaste")
else:
    print(f"\nHas perdido. La palabra era '{palabra}'.")


