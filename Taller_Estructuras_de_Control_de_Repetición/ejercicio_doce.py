listaPuntaje=[]
listaNombres=[]
cantidad=int(input("Introduzca la cantidad de estudiantes "))
i=0
sumatoria=0
promedio=0

while (i<cantidad):
    nombre=str(input("Indique el nombre del estudiante "))
    puntaje=float(input("Indique el puntaje del estudiante "))
    listaNombres.append(nombre)
    listaPuntaje.append(puntaje)
    sumatoria=sumatoria+listaPuntaje[i]
    i=i+1
print(sumatoria)
promedio=sumatoria/cantidad
print(f"El promedio de las calificaciones es: {promedio}")
maximo=max(listaPuntaje)
minimo=min(listaPuntaje)
indiceMax=(listaPuntaje.index(maximo))
indiceMin=(listaPuntaje.index(minimo))
print(indiceMax)
print(indiceMin)
print(f"La mayor nota es de: {listaNombres[indiceMax]}, con el puntaje de: {listaPuntaje[indiceMax]}")
print(f"La menor nota es de: {listaNombres[indiceMin]}, con el puntaje de: {listaPuntaje[indiceMin]}")

