monto=float(input("Escriba el monto a invertir"))
montoint=float(input("Escriba el monto  de interés"))


interes=(monto*(montoint/100))
montofin=(interes+monto)

if (interes>100000):
    print(f"El monto invertido es de ${interes} pesos , el cual supera la cantidad de $100.000 pesos")
else:
    print(f"El monto invertido es de ${interes} pesos , el cual no supera la cantidad de $100.000 pesos")


print(f"El monto total de su cuenta es de ${montofin} pesos")