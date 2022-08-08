p=float(input("Introduzca el precio del computador"))
c=float(input("digite precio por cuota"))

precio=(((c)-(p/12)))
interes=((precio*100)/c)
interes1=round(interes,2)

print(f"El porcentaje de ganancia por cada cuota es de: {interes1}%")