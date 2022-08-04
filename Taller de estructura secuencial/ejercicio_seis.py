vm=int(input("Introduzca el número de mujeres en la clase: "))
vh=int(input("Introduzca el número de hombres en la clase"))

total=(vh+vm)
porcentajem=((vm*100)/total)
procentajeh=((vh*100)/total)

print(f"El procentaje de mujeres en la clase es de: {porcentajem}% de {total} , El número de hombres es de: {procentajeh}% de {total}")