listaNombres=[]
listaPuntaje=[]
listaCarrera=[]
n=int(input("Introduzca el número de estudiantes "))
i=1

while (n>0):
    est= str(input(f"Introduza el nombre del estudiante #{i}"))
    listaNombres.append(est)
    carrera=str(input("Indique la carrera del estudiante "))
    puntaje=float(input("Indique el puntaje del estudiante "))
    listaCarrera.append(carrera)
    listaPuntaje.append(puntaje)
    i=i+1
    n=n-1

print(f"{listaNombres}, {listaCarrera}, {listaPuntaje}")