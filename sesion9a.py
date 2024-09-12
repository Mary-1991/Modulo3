def calcular_area_rectangulo():
    try:
        # Solicitar la base y altura al usuario
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))

        # Validar que ambos números sean positivos
        if base <= 0 or altura <= 0:
            return "Error: Ambos parámetros deben ser números positivos."

        # Calcular el área
        area = base * altura
        return f"El área del rectángulo es: {area}"

    except ValueError:
        return "Error: Ambos parámetros deben ser números."

# Llamar a la función
resultado = calcular_area_rectangulo()
print(resultado)

