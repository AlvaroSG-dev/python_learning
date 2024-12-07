import random

# Diccionario para contar las apariciones de "Cara" y "Cruz"
resultados = {"Cara": 0, "Cruz": 0}

print("Lanzamientos de moneda:")

# Simulación de 10 lanzamientos
for _ in range(10):
    resultado = random.choice(["Cara", "Cruz"])
    print(resultado)
    resultados[resultado] += 1

print("\nResultados finales:")
print(f"Cara: {resultados['Cara']} veces")
print(f"Cruz: {resultados['Cruz']} veces")
