# Definir la palabra y las vocales
palabra = "paralelepípedo"
vocales = "aeiouáéíóú"

# Crear una lista para almacenar las consonantes y sus posiciones
consonantes = []

# Recorrer la palabra y almacenar las consonantes junto con su posición
for indice, letra in enumerate(palabra):
    if letra not in vocales:
        consonantes.append((letra, indice))

# Imprimir las consonantes y sus posiciones
for consonante, posicion in consonantes:
    print(f"Consonante: {consonante}, Posición: {posicion}")
