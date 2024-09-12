# Crear una lista con 10 números enteros
numeros = [30, -8, 0, 70, 15, 9, 32, 5, -2, 0]

# Recorrer la lista con un bucle for
for numero in numeros:
    if numero == 0:
        print(f"{numero} es cero.")
    elif numero % 2 == 0:
        print(f"{numero} es par.")
    else:
        print(f"{numero} es impar.")
