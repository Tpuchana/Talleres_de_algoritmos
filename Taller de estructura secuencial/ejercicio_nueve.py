salariobase=float(input("Escriba su salario base: "))
preciohoras=float(input("Escriba el precio por hora"))
horas=int(input("Escriba las horas trabajadas"))

salariototal=(((salariobase)-(salariobase*0.20))+(preciohoras*horas))

print(f"El salario total del trabajador es de: {salariototal}")