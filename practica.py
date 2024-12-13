import time

def decorador(funcion):
    def interior(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        final = time.time()
        print(f"El tiempo de ejecucion es de: {(final - inicio):.5f}")
        return resultado
    return interior

@decorador
def factorial(n):
    multi = 1
    for i in range(1, n + 1):
        multi = multi * i
    return multi

resultado = factorial(1000)
print(f"El factorial es: {resultado}")


def funcionDecorador(funcion):
    def interno(
            
    ):
        error = True
        while error == True:  
            try:
                a = int(input("Ingrese el valor de a: "))
                b = int(input("Ingrese el valor de b: "))
                resultado = funcion(a, b)
            except ZeroDivisionError:
                print("La division no puede ser cero")
            else: 
                error = False
                print("Calculando...")
        return resultado
    return interno

@funcionDecorador
def division(a, b):
    return a / b

resultado = division()
print(f"El resultado de la division es: {resultado:.1f}")
