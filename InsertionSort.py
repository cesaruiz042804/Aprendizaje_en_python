array = [10, 4, 1, 67,34, 2, 1, 6]
array2 = array.copy() ### Es to sirve para copiar los valores de un array a otro

n = len(array) ### len es para saber el tamaño de un arreglo

for i in range(n):
    min = i ### Aqui sigue el ciclo normal de 0, 1, 2, 3, 4....
    aux = array[i]
    while(min > 0 and array[min - 1] > aux): ## Esto se repetira hasta que min no sea menor a cero o igual a cero
        ### Se va verificando de derecha a izquierda hasta el mismo numero encuentre a alguien menor
        array[min - 1], array[min] = array[min], array[min - 1]
        min = min - 1

print(array2)
print(array)