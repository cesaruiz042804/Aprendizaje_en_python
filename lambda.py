# A lado se ponen las variables que se van a usar, y a lado las operaciones

suma = lambda a, b : a + b
funcion = lambda x, a, b, c : ((a) * (x**2)) + (b * x) + c # ax^2 + bx + c


x = int(input('Ingrese el valor de x: '))
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

print('Resultado funcion: ', funcion(x, a, b, c))
print('Resultado suma: ', suma(a, b))


