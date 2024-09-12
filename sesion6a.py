# Programa para analizar un número

# Solicitamos al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Evaluamos si el número es cero
if numero == 0:
    print("El número es cero.")
else:
    # Evaluamos si el número es positivo
    if numero > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
    
    # Evaluamos si el número es par o impar
    if numero % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")
