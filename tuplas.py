print('')

tupla_vacia = () # tupla vacia

print('Tupla vacia: ', tupla_vacia)

tupla = (1, "Hola", True, 4, 20)
print(tupla)

# concatenacion de tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_combinada = tupla1 + tupla2 # concatenacion de tuplas
print('Concatenacion de tupla: ', tupla_combinada)

# Desempaquetado básico
mi_tupla = (1, 2, 3)
a, b, c = mi_tupla

print('Valor de a: ', a) 
print('Valor de b: ', b) 
print('Valor de c: ', c) 

mi_tupla_anidada = ((1, 2, 9, 5), (3, 4), (5, 6, 4))

# Desempaquetado de tuplas anidadas
(tupla1, tupla2, tupla3) = mi_tupla_anidada

print('Tupla 1: ', tupla1) 
print('Tupla 2: ', tupla2) 
print('Tupla 3: ', tupla3)

# Desempaquetado con asterisco
mi_tupla = (1, 2, 3, 4, 5)

# Desempaquetado con asterisco
primero, segundo, *resto = mi_tupla # El asterisco toma todos los demas valores

print('Primero: ', primero)
print('Segundo: ', segundo)
print('Resto: ', resto)

# Desempaquetado con guión bajo (_)
mi_tupla = (1, 2, 3, 4, 5)

# Desempaquetado con guión bajo
primero, _, tercero, _, quinto = mi_tupla

print('Primero: ', primero)
print('Tercero: ', tercero) 
print('Quinto: ', quinto)

# Conversion de tuplas a listas 
mi_tupla = (1, 'Hola', 34, True)
mi_lista = list(mi_tupla)
print(mi_lista)

# Pertenencia en tuplas 
if "Hola" in mi_tupla:
    print('Hola esta en la tupla')

# Repetición
repeticion = mi_tupla * 2
print(repeticion)

"""""

Tuplas en Python
Las tuplas en Python son estructuras de datos que almacenan 
colecciones ordenadas de elementos. Son similares a las listas, 
pero con una diferencia crucial: las tuplas son inmutables, 
lo que significa que no se pueden modificar una vez creadas.


"""""