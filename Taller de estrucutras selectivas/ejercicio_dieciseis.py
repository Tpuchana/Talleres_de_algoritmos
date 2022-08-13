import math
a=int(input("Digite valor de A "))
b=int(input("Digite valor de B "))
c=int(input("Digite valor de C "))
x=int(input("Digite valor de X "))

eq=((a*x**2)+(b*x)+(c))
d=((b**2)-(4*a*c))

if d==0:
    formu=(b/(2*a))
    print(f"{formu}")
if d>0:
    formu1=(b + math.sqrt(b**24*a*c))/(2*a)
    
    print(f"{formu1}")
if d<0:
    print(f"No tiene solución en los reales")
