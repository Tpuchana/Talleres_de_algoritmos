cat=int(input("Digite la categoría a la que pertenece como trabajador "))

if cat==1:
    uno=(5000000+(5000000*0.10))
    print(f"Usted pertenece a la categoría {cat}, su sueldo es de 5000000, con el aumento del 10% es de {uno} ")
elif cat==2:
    dos=(4300000+(4300000*0.15))
    print(f"Usted pertenece a la categoría {cat}, su sueldo es de 4300000, con el aumento del 15% es de {dos} ")
elif cat==3:
    tres=(3600000+(3600000*0.20))
    print(f"Usted pertenece a la categoría {cat}, su sueldo es de 3600000, con el aumento del 20% es de {tres} ")
elif cat==4:
    cuatro=(2000000+(2000000*0.40))
    print(f"Usted pertenece a la categoría {cat}, su sueldo es de 2000000, con el aumento del 40% es de {cuatro} ")
elif cat==5:
    cinco=(900000+(900000*0.60))
    print(f"Usted pertenece a la categoría {cat}, su sueldo es de 900000, con el aumento del 60% es de {cinco} ")
elif cat>5:
    print(f"Categoría inválida")
elif 1>cat:
    print(f"Categoría inválida")