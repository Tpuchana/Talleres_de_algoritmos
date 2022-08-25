lista=[]
n=int(input("Introduzca el número de estudiantes "))
i=1

while (n>0):
    estatura= int(input(f"Estudiante {i}: "))
    lista.append(estatura)
    i=i+1
    n=n-1

print(f"La lista de estaturas es de: {lista}")