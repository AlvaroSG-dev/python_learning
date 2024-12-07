frase = input("introduce frase: ")
palabras = frase.lower().split()
posiciones= {}
for i in range(len(palabras)):
    palabra = palabras[i]
    if palabra not in posiciones:
        posiciones[palabra]= []
    posiciones[palabra].append(i)
    


print(posiciones)