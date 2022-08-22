lista=[]
n=int(input("Introduzca el número de estudiantes "))
i=1

while (n>0):
    estatura= float(input(f"Estatura# {i}: "))
    lista.append(estatura)
    i=i+1
    n=n-1

mayor=max(lista)
print(f"Lista: {lista}")
print(f"Mayor estatura: {mayor}")








