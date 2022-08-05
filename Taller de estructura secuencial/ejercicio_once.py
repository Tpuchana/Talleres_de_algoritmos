nombre=str(input("¿Cuál es su nombre?"))
horas=int(input("¿Cuántas horas ha trabajado?"))
pago=float(input("¿Cuánto cobra por hora?"))
horax=int(input("¿Cuántas horas extra ha trabajado?"))
hijo=int(input("¿Cuántos hijos tiene?"))


sueldobase=((horas*pago))
reducciones=(sueldobase-(sueldobase*0.14))
asignaciones=(reducciones+180000+173000+250000)
horasextra=((horax)*(pago*0.25))
sueldototal=(horasextra+asignaciones)

print(f"Hola {nombre} , usted cuenta con un sueldo neto de: {sueldototal} para el mes de diciembre ")