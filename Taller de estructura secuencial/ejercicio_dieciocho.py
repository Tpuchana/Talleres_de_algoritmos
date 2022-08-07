bolivar=float(input("Digite la cantidad de bolivares"))
bolivard=float(input("Digite la cantidad de bolivares después del impuesto"))


razon=(bolivard/bolivar)
impuesto=(razon*4*bolivar)/100

print(f"El total de impuesto cobrado fue de: {impuesto}")
