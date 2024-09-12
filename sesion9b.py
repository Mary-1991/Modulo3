# Función para sumar dos números
def sumar(a, b):
    return a + b

# Función para restar dos números
def restar(a, b):
    return a - b

# Función para multiplicar dos números
def multiplicar(a, b):
    return a * b

# Función para dividir dos números
def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

# Función que acepta dos números y regresa una tupla con los resultados de las operaciones
def realizar_operaciones(a, b):
    suma = sumar(a, b)
    resta = restar(a, b)
    multiplicacion = multiplicar(a, b)
    division = dividir(a, b)
    return (suma, resta, multiplicacion, division)

# Función para solicitar los números y almacenar los resultados en un diccionario
def calcular_y_almacenar_resultados():
    try:
        # Solicitar números al usuario
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        # Realizar las operaciones
        resultados = realizar_operaciones(a, b)
        
        # Almacenar los resultados en un diccionario
        diccionario_resultados = {
            "Suma": resultados[0],
            "Resta": resultados[1],
            "Multiplicación": resultados[2],
            "División": resultados[3]
        }
        
        return diccionario_resultados
    
    except ValueError:
        return "Error: Ambos parámetros deben ser números."

# Llamar a la función para ejecutar el código
resultados = calcular_y_almacenar_resultados()
print(resultados)
