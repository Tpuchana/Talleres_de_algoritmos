sueldo=float(input("Digite el sueldo del trabajador"))

if sueldo<900000:
    sueldo1=sueldo+(sueldo*0.15)
    print(f"Su sueldo con el aumento es de {sueldo1}")
else:
    sueldo2=sueldo+(sueldo*0.12)
    print(f"Su sueldo con el aumento es de {sueldo2}")