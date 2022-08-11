datos=(input("Ingrese los datos A,B,C y D "))
print(datos)
(a,b,c,d)=datos.split(" ")
a=int(a)
b=int(b)
c=int(c)
d=int(d)

if d==0:
    resultado1=(a-c)**2
    print(f"El resultado es: {resultado1}")
else:
    resultado2=(((a-c)**3)/d)
    print(f"El resultado es {resultado2}")

