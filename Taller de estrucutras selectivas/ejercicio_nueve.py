nombre=str(input("Introduzca su nombre "))
compra=float(input("Introduzca el monto de la compra del cliente "))

if compra<50000:
    print(f"Sr/a {nombre}, No se efectúa el descuento, por lo tanto la compra es de ${compra} pesos")
elif 50000<=compra<100000:
    des=(compra-(compra*0.05))
    print(f"Sr/a {nombre}, Se efectúa el descuento del 5%, por lo tanto la compra es de ${des} pesos")
elif 100000<=compra<700000:
    des1=(compra-(compra*0.11))
    print(f"Sr/a {nombre}, Se efectúa el descuento del 11%, por lo tanto la compra es de ${des1} pesos")
elif 700000<=compra<1500000:
    des2=(compra-(compra*0.18))
    print(f"Sr/a {nombre}, Se efectúa el descuento del 18%, por lo tanto la compra es de ${des2} pesos")
elif compra>1500000:
    des3=(compra-(compra*0.25))
    print(f"Sr/a {nombre}, Se efectúa el descuento del 25%, por lo tanto la compra es de ${des3} pesos") 