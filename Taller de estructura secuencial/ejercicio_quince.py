pvf=float(input("Introduzca el precio final pagado por el producto"))
pvp=float(input("Introduzca el precio para el público del producto"))

diferencia=(pvf-pvp)
descuento=((diferencia*100)/(pvf))
descre=round(descuento, 2)

print(f"El descuento aplicado para el precio para público es de: {descre} %")