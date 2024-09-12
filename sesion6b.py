# Programa para ordenar tres números de mayor a menor

# Solicitamos al usuario que ingrese tres números diferentes
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

# Evaluamos el orden de los números
if num1 > num2:
    if num1 > num3:
        if num2 > num3:
            print(f"El orden es: {num1}, {num2}, {num3}")
        else:
            print(f"El orden es: {num1}, {num3}, {num2}")
    else:
        print(f"El orden es: {num3}, {num1}, {num2}")
else:
    if num2 > num3:
        if num1 > num3:
            print(f"El orden es: {num2}, {num1}, {num3}")
        else:
            print(f"El orden es: {num2}, {num3}, {num1}")
    else:
        print(f"El orden es: {num3}, {num2}, {num1}")
