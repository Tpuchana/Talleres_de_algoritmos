valorin=float(input("Ingresar lectura inicial de consumo"))
valorfin=float(input("Ingresar lectura final de consumo"))

costo=((valorfin-valorin)*(269.79))

print(f"Usted debe pagar {costo} pesos por su consumo energético de este mes")