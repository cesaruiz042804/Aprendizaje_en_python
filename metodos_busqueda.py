print('Métodos de búsqueda')
numeros = [1, 45, 100, 23, 4, 67, 12, 100, 22, 56, 43]
print(numeros)

incluido = 100 in numeros
print('in: ', incluido)

indice = numeros.index(4)
print('index: ', indice)

cont = numeros.count(100)
print('count: ', cont)


"""""
Métodos de búsqueda:

in(elemento): Verifica si el elemento especificado se encuentra en el arreglo.
index(elemento): Devuelve el índice de la primera ocurrencia del elemento especificado en el arreglo.
count(elemento): Cuenta el número de veces que aparece el elemento especificado en el arreglo.

"""""