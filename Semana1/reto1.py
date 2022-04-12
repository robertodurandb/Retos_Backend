
# """Reto 1: Desarrollar un programa de bienvenida: """
nom=""
nom=input("Ingrese su nombre:")
edad=int(input("Ingrese su edad:"))

print("Bienvenido ",nom)
print("su edad es: ",edad)

if edad>=18:
    print("Es usted mayor de edad")
    print("Estimado ",nom," no esta obligado a hacer nada")
else:
    print("Es usted menor de edad")
    print("Estimado ",nom," si es mas de las 6pm debe ir a dormir y si no hacer la tarea")
