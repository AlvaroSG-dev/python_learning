def sumar(num1,num2):
    return num1 +num2
def restar(num1,num2):
    return num1 - num2
def multiplicar(num1,num2):
    return num1 * num2
def dividir(num1,num2):
    if num2== 0:
        return "Error: no se puede dividir entre cero"
    return num1/num2

def calculadora():
    while True:
        print("\n=== Calculadora ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Elige una opción (1-5): ")
        if opcion in ["1", "2", "3", "4"]:
            try:
                num1= float(input("Introduce el primer numero: "))
                num2 = float(input("Introduce el segundo numero: "))
                if opcion == "1":
                    print(f"{num1} + {num2} = {sumar(num1,num2)} ")
                elif opcion == "2":
                    print(f"{num1} + {num2} = {restar(num1,num2)} ")
                elif opcion == "3":
                    print(f"{num1} + {num2} = {multiplicar(num1,num2)} ")
                elif opcion == "4":
                    print(f"{num1} + {num2} = {dividir(num1,num2)} ")
            except ValueError:
                print(f"Introduce números validos")
        elif opcion == "5":
            print("Saliendo de la calculadora")
            break
        else:
            print("Opcion no valida. Por favor elije un numero de 1-5")


calculadora()
