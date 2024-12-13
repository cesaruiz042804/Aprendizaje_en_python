cant = int(input('Cantidad de números a guardar: '))

miLista = []

for i in range(cant):
    miLista.append(int(input('Ingresa un número: ' )))

miLista2 = miLista.copy()

for i in range(cant):
    for j in range(cant - i - 1):
        print(miLista)
        if(miLista[j] > miLista[j + 1]):
            miLista[j], miLista[j + 1] = miLista[j + 1], miLista[j] 
            ###técnica llamada "empaquetado y desempaquetado de tuplas" (tuple packing and unpacking).
            """""
            n = miLista[j]
            miLista[j] = miLista[j + 1]
            miLista[j + 1] = n
            """""

print('Primer arreglo: ', miLista2)
print('Segundo arreglo: ', miLista)

### El metodo de ordenamiento de burbuja compara por ejemplo el indice 0 y el 1 y los intercambia