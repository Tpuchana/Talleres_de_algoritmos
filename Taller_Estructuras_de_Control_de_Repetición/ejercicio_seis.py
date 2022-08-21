from os import kill


n=int(input("Introduzca un número entero "))
k=int(input("Introduzca otro número "))
r=0
c=n
d=(n/k)

while (c>0):
    c=c-k
    r=r+1
    print(c)

print(f"{r} es el número de restas efectuadas")
    


