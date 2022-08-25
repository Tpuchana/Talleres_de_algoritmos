lista=[]
n=int(input("Introduzca el número de estudiantes "))
i=1

while (n>0):
    edad= int(input(f"Estudiante {i}: "))
    lista.append(edad)
    i=i+1
    n=n-1

print(f"La lista de edades es de: {lista}")