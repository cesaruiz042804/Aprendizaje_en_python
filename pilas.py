from collections import deque
# Cola de doble extremo

pila = deque()

pila.append(10)
pila.append(6)
pila.append(22)
pila.append(9)
pila.append(1)
pila.append(44)
pila.append(2)

print(pila)

pila.pop()
pila.pop()


print(pila)