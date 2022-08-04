n1=float(input("Introduzca la nota del primer parcial"))
n2=float(input("Introduzca la nota del segundo parcial"))
n3=float(input("Introduzca la nota del tercer parcial"))
ef=float(input("Introduzca la nota del examen final"))
tf=float(input("Introduzca la nota del trabajo final"))

promedio=((((n1+n2+n3)/(3))*(0.55))+(ef*0.30)+(tf*0.15))

print(f"Su nota final es de: {promedio}")