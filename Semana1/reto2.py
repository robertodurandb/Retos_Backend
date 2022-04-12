from datetime import date, datetime

totalp=0
lista = []
factual = date.today()
print("Fecha actual: ",factual)
totalp=int(input("Ingrese el total de personas:  "))

class Persona:
    def __init__(self, nombre, dni, fechanac, edad):
        self.nombre=nombre
        self.dni=dni
        self.fechanac=fechanac
        self.edad=edad
    def __repr__(self):
        return (f'\nEdad: {self.edad} Nombre: {self.nombre} Dni: {self.dni}  Fecha Nacimiento: {self.fechanac}\n'
        )

for i in range(totalp):
    persona1=Persona(input("nombre:"),input("dni:"),input("fecha de nacimiento:"),0)
    fnac=datetime.strptime(persona1.fechanac, '%d-%m-%Y')
    edad = factual.year - fnac.year
    persona1.edad=edad
    print("****objeto agregado a la lista****")
    lista.append(persona1)

lista.sort(key=lambda x:x.edad)
print("\nIMPRESION ORDENADA POR EDADES:\n")
print(repr(lista))




