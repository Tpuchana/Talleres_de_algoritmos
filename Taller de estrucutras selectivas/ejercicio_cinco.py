sueldo=float(input("Digite el sueldo bruto mensual de los trabajadores"))
v1=float(input("Digite las ventas del primer departamento"))
v2=float(input("Digite las ventas del segundo departamento"))
v3=float(input("Digite las ventas del tercer departamento"))

vt=(v1+v2+v3)
por=(vt*0.33)
ex=(sueldo+(sueldo*0.20))

if v1>por and v2<por and v3<por:
    print(f"En el primer departamento ganaron $ {ex} de pesos, en el segundo departamento y el tercero ganaron ${sueldo} de pesos")
elif v2>por and v1<por and v3<por:
     print(f"En el segundo departamento ganaron $ {ex} de pesos, en el primero departamento y el tercero ganaron ${sueldo} de pesos")
elif v3>por and v2<por and v1<por:
     print(f"En el tercer departamento ganaron $ {ex} de pesos, en el primero departamento y el segundo ganaron ${sueldo} de pesos")
elif v1>por and v2>por and v3<por:
    print(f"En el tercer departamento ganaron $ {sueldo} de pesos, en el primer departamento y el segundo ganaron ${ex} de pesos")
elif v1>por and v3>por and v2<por:
    print(f"En el segundo departamento ganaron $ {sueldo} de pesos, en el primer departamento y el tercero ganaron ${ex} de pesos")
elif v2>por and v3>por and v1<por:
    print(f"En el primer departamento ganaron $ {sueldo} de pesos, en el tercer departamento y el segundo ganaron ${ex} de pesos")
elif v2>por and v3>por and v1>por:
    print(f"En los tres departamentos ganaron ${ex} de pesos")
