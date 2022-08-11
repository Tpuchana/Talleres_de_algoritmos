v=float(input("Introduzca la velocidad del vehículo "))

if 300<v>1000:
    pago=(150000+((v-1000)*9000))
    print(f"El cliente debe de pagar ${pago} pesos")
elif 300<v<1000:
    pago1=(70000+((v-300)*30000))
    print(f"El cliente debe de pagar ${pago1} pesos")
elif 300>v:
    print(f"El cliente debe de pagar $50.000 pesos")