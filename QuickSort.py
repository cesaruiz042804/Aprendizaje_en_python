array = [10, 4, 1, 67,34, 2, 1, 6, 12, 61, 23, 3, 6, 100]

array2 = array.copy()

print(array)

def QuickSort(array):
    print('Array inicio: ', array)
    if(len(array) < 1):
        print('Array vacio')
        return []

    left = []
    right = []
    pivot = array[0]

    for i in range(1, len(array)):
        if(array[i] < pivot): ### Si se cumple, los valores menores al pivote se van al array left
            left.append(array[i])
        else:
            right.append(array[i]) ### Si se cumple, los valores menores al pivote se van al array right

    print('left: ', left)
    print('right: ', right)
    return (QuickSort(left) + [pivot] + QuickSort(right))
    ### Aca se van uniendo todos los mini array de cada recursividad que va pasando

array = QuickSort(array)

print(array)