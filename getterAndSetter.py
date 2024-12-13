class Persona:

    def __init__(self, nombre, edad):
        self.name = nombre
        self.old = edad

    def getNombre(self):  
        return self.name
    
    def setNombre(self, name):
        self.name = name

    def getEdad(self):
        return self.old
    
    def setNombre(self, old):
        self.old = old

    def Imprimir(self):
        if(self.old < 18):
            print(self.name, ' es menor de edad')
        else:
            print(self.name, ' es mayor de edad')

nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
persona = Persona(nombre, edad)
persona.Imprimir()
