print('Métodos básicos de manipulación')

numeros = [1, 45, 100, 23, 4, 67, 12]
print(numeros)
numeros.append(50)
numeros.append(69)
print('append: ',numeros)

numeros.insert(3, 70)
print('insert: ', numeros)

numeros.remove(67)
print('remove', numeros)

numeros.pop(2)
print('pop: ', numeros)

numeros.clear()
print('clear: ', numeros)

numeros = [9, 23, 45, 12, 44, 89]
print('Nuevos valores: ', numeros)
tam = len(numeros)
print('Tamaño del arreglo: ', tam)


""""
Métodos básicos de manipulación:

append(elemento): Agrega un nuevo elemento al final del arreglo.
insert(indice, elemento): Inserta un nuevo elemento en el índice especificado del arreglo.
remove(elemento): Elimina la primera ocurrencia del elemento especificado del arreglo.
pop([indice]): Elimina el elemento en el índice especificado (o el último si no se indica) y lo devuelve.
clear(): Elimina todos los elementos del arreglo.
len(arreglo): Devuelve la longitud del arreglo (cantidad de elementos).

"""