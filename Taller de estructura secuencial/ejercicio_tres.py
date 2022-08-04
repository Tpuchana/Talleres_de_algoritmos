sueldo=float(input("Escriba su sueldo: "))
v1=float(input("Escriba el monto de su primera venta: "))
v2=float(input("Escriba el monto de su segunda venta: "))
v3=float(input("Escriba el monto de su tercera venta: "))

comision=((v1+v2+v3)*(0.10))
sueldot=((comision)+(sueldo))


print(f"Comisión: {comision} , Sueldo total: {sueldot}")
