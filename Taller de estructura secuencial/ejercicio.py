import math
datos=(input(""))
print(datos)
(a,b,c)=datos.split(" ")
a=float(a)
b=float(b)
c=float(c)
raiz=b**2-4*a*c
denominador=2*a
if(denominador==0 or raiz<0):
    print("Impossivel calcular")
else:
    r1=(-b+math.sqrt(raiz))/denominador
    r2=((-b-math.sqrt(raiz))/denominador)
    print(f"R1 = {round(r1,5)}")
    print(f"R2 = {round(r2,5)}")

print(a,b,c)
