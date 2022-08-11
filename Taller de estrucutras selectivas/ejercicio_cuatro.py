paga=float(input("Ingrese el valor a pagar de la compra"))

if paga>5000000:
    x=(paga*0.55)
    print(f"La empresa invierte ${x} pesos, el 55%")
    b=(paga*0.30)
    print(f"La empresa pide prestado ${b} pesos al banco, el 30%")
    f=(paga-(x+b))
    interes=(paga+(f*0.20))
    print(f"La empresa debe pagar ${interes} pesos, esto debido a la suma de la comisión de los fabricantes")
else:
    x1=(paga*0.70)
    print(f"La empresa invierte ${x1} pesos, el 70%")
    f1=(paga*0.30)
    print(f"Al solicitar crédito a los fabricantes, estos pagarían ${f1} pesos")
    interes1=((paga-x1)*0.20)
    tot=(paga+interes1)
    print(f"La empresa debe pagar ${tot} pesos, esto debido a la suma de la comisión de los fabricantes")