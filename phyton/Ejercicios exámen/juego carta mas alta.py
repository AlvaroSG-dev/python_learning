import random

valores = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
palos = ["Corazones", "Diamantes", "Tréboles", "Picas"]
baraja_Entera = []
jugador= []
for i in range (0,len(valores)):

    for j in range (0, len(palos)):
        tupla = (valores[i]),(palos[j])
        baraja_Entera.append(tupla)
        
random.shuffle(baraja_Entera)

for i in range (0,5):
    jugador.append(baraja_Entera[i])

mayor = [("2", "picas")]
for i in range(0,5):
    if valores.index(jugador[i][0])> valores.index(mayor[0][0]):
        mayor = jugador[i]

print("Tu mano es: ",jugador)
print("Tu carta mas alta es: ",mayor)


    


