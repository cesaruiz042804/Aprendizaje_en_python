print('Métodos de ordenamiento')
numeros = [1, 45, 100, 23, 4, 67, 12, 100, 22, 56, 43]

ascendente = sorted(numeros)
descendente = sorted(numeros, reverse = True)

print('sorted ascendente: ', ascendente)
print('sorted descendente: ', descendente)

numeros.sort()
print('sort ascendente: ', numeros)
numeros.sort(reverse = True)
print('sort descendente: ', numeros)


"""""
Métodos de ordenamiento:

Utilizando la función sorted():

La función sorted() de Python crea una nueva lista ordenada, 
sin modificar la lista original. Puedes especificar el orden de clasificación 
(ascendente o descendente) utilizando el argumento reverse.
sort([key]): Ordena los elementos del arreglo en orden ascendente (o descendente si se especifica la función key).
sorted(arreglo, [key]): Devuelve una copia ordenada del arreglo (sin modificar el arreglo original).

"""""