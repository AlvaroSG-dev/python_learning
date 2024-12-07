alt= float(input("Inserte altura en cm:"))
anch= float(input("Inserte anchura en cm:"))
area= anch*alt
Pbandera= area *0.01
escudo = input("¿Quiere escudo bordado? (s/n): ").strip().lower()

if escudo == "s":
    Pescudo= 2.50
else:
    Pescudo= 0.0
envio= 3.25
total= Pescudo+Pbandera+envio

print("\nGracias. Aquí tiene el desglose de su compra.")
print(f"Bandera de {int(area)} cm²: {Pbandera:.2f} €")
print(f"{'Con' if escudo == 's' else 'Sin'} escudo: {Pescudo:.2f} €")
print(f"Gastos de envío: {envio:.2f} €")
print(f"Total: {total:.2f} €")