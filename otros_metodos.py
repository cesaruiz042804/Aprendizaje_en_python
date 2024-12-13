print('Métodos de concatenación')
numeros = [1, 45, 100, 23, 4, 67]
print(numeros)

otros = [12, 100, 22, 56, 43]

numeros.extend(otros)
print('extend: ', numeros)

str(numeros)
print('str: ', numeros)




"""""
Métodos de concatenación:

+: Concatena dos arreglos en uno nuevo.
extend(otro_arreglo): Añade todos los elementos de otro arreglo al final del arreglo original.
Métodos de conversión:

str(): Convierte el arreglo en una cadena de caracteres que representa sus elementos.
list(iterable): Convierte un iterable (como una cadena o un conjunto) en un arreglo.
Métodos adicionales:

copy(): Devuelve una copia completa del arreglo.

"""""
