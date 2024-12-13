array = [10, 4, 1, 67,34, 2, 1, 6]

### array2 = array esto no es util
array2 = array.copy()

size = len(array)

for i in range(size - 1):
    min = i
    for j in range(i + 1, size):
        if(array[j] < array[min]):
            min = j
    if(i != min):
        array[i], array[min] = array[min], array[i]

print(array2)
print(array)

### El metodo de ordenamiento de seleccion busca el valor mas bajo segun su indice