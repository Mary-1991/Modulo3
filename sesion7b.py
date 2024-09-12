# Lista de diccionarios que representa la información de los estudiantes
estudiantes = [
    {'nombre': 'Juan', 'edad': 17, 'calificaciones': [85, 90, 88]},
    {'nombre': 'María', 'edad': 19, 'calificaciones': [92, 89, 90]},
    {'nombre': 'Pedro', 'edad': 21, 'calificaciones': [85, 95, 80]},
    {'nombre': 'Ana', 'edad': 18, 'calificaciones': [90, 92, 87]},
    {'nombre': 'Luis', 'edad': 20, 'calificaciones': [88, 85, 92]},
]

# Función para calcular el promedio de una lista de números
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)

# Función para determinar si un número es primo
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Filtrar y mostrar estudiantes con más de 18 años y promedio > 85
print("Estudiantes con más de 18 años y promedio superior a 85:")
for estudiante in estudiantes:
    edad = estudiante['edad']
    promedio = calcular_promedio(estudiante['calificaciones'])
    
    if edad > 18 and promedio > 85:
        print(f"Nombre: {estudiante['nombre']}, Edad: {edad}, Promedio: {promedio:.2f}")

# Calcular el promedio de calificaciones para estudiantes con edad > 18 y edad primo
promedio_total = 0
contador = 0

print("\nEstudiantes con más de 18 años y edad primo:")
for estudiante in estudiantes:
    edad = estudiante['edad']
    if edad > 18 and es_primo(edad):
        promedio = calcular_promedio(estudiante['calificaciones'])
        print(f"Nombre: {estudiante['nombre']}, Edad: {edad}, Promedio: {promedio:.2f}")
        promedio_total += promedio
        contador += 1

if contador > 0:
    promedio_final = promedio_total / contador
    print(f"\nPromedio de calificaciones de estudiantes con edad primo y > 18: {promedio_final:.2f}")
else:
    print("\nNo hay estudiantes con más de 18 años cuya edad sea un número primo.")
