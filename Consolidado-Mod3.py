# Lista de nombres
nombres = ['Harry Houdini', 'Newton', 'David Blaine', 'Hawking', 'Messi', 'Teller', 'Einstein', 'Pele', 'Juanes']

# Separar nombres en tres grupos: magos, científicos y otros
magos = ['Harry Houdini', 'David Blaine', 'Teller']
cientificos = ['Newton', 'Hawking', 'Einstein']
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# Función para modificar la lista de magos
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = 'El gran ' + lista_magos[i]

# Función para imprimir nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir la lista completa antes de modificar
print("Lista completa antes de modificar:")
imprimir_nombres(nombres)
print("\n")

# Modificar la lista de magos
hacer_grandioso(magos)

# Imprimir los nombres de los magos grandiosos, científicos y otros
print("Magos grandiosos:")
imprimir_nombres(magos)
print("\nCientíficos:")
imprimir_nombres(cientificos)
print("\nOtros:")
imprimir_nombres(otros)

