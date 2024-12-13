def funcionDecorador(funcion):
    def funcionalidades():
        print("El calculo es:")
        funcion()
        print("Aqui hemos terminado el calculo")
    return funcionalidades # Se tiene que retornar la funcion

@funcionDecorador
def suma():
    print(f"Suma: {4 + 2}")

@funcionDecorador
def resta():
    print(f"Resta: {5 - 3}")

suma()
resta()








