array = [10, 4, 23, 67, 28, 29, 2, 7, 11, 56, 67, 32]
#array = [2, 4, 7, 10, 11, 23, 28, 29, 32, 56, 67, 67]
print(array)
array.sort()
print(array)
num = int(input("Ingrese el numero que quiere buscar: "))

def buscar(num, array):
    inicio = 0
    final = len(array) - 1

    while(inicio <= final):
        centro = (inicio + final) // 2 # Las dos barras son para volver la division en un entero 
        if(array[centro] == num):
            return centro
        elif(array[centro] < num):
            inicio = centro + 1
        else:
            final = centro - 1
    return False

indice = buscar(num, array)
if indice == False:
    print("El numero no existe dentro del array")
else:
    print(f"El numero {array[indice]} se encuentra en el indice {indice} ")