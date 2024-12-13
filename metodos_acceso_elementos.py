print('Métodos de acceso a elementos')

numeros = [1, 45, 100, 23, 4, 67, 12, 100, 22, 56, 43]
print(numeros)

indice = 2
print(numeros[indice])

print(numeros[:indice])

print(numeros[2 : 5])

numeros2 = numeros[:]
print(numeros2)

"""""
Métodos de acceso a elementos:

arreglo[indice]: Obtiene el elemento en el índice especificado del arreglo.
arreglo[:indice_final]: Obtiene una sublista desde el principio del 
arreglo hasta el índice especificado (sin incluirlo).
arreglo[indice_inicial:indice_final]: Obtiene una sublista desde el índice 
inicial (incluido) hasta el índice final (sin incluirlo).
arreglo[:]: Obtiene una copia completa del arreglo.

"""""