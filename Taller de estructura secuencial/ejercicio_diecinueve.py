n=int(input("Digite el número de naranjas comprados: "))
d=float(input("Digite el precio en el que venderá las docenas: "))
v=float(input("Digite el monto que obtuvo después de vender: "))

pd=((n/12)*d)
venta=(((v-pd)*(100))/pd)

print(f"Usted obtuvo una ganancia del {venta} %")

