import queue

cola = queue.Queue()

cola.put(8)
cola.put(56)
cola.put(1)
cola.put(12)
cola.put(100)
cola.put(67)

lista = list(cola.queue)
print(lista)

eliminado = cola.get()

print(eliminado)


"""""
put(elemento): Agrega un elemento al final de la cola.
get(): Elimina y devuelve el primer elemento agregado a la cola.
empty(): Comprueba si la cola está vacía.
"""""
