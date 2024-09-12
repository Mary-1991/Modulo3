mi_list=([list[1,2,3],list[0,4,5], list[4,0,1], list[6,5,4]])
mi_list.remove(list[0,4,5])
print(mi_list)

# Lista original
lista_anidada = [list([1, 2, 3]), list([4, 0, 1]), list([6, 5, 4])]

# Eliminar los ceros de cada sublista
lista_sin_ceros = [[num for num in sublista if num != 0] for sublista in lista_anidada]

# Imprimir la lista resultante
print(lista_sin_ceros)

#Crear diccionario:
mi_diccionario={'A':[1, 2, 3],'B':[4,1],'C':[6, 5, 4]}
print(mi_diccionario)
