lista=[]
n=int(input("Introduzca el número de países "))
i=1

while (n>0):
    pais= (input("Introduza un país"))
    capital=input("Digite capital")
    org=(pais,capital)
    lista.append(org)
    if (pais=="" and capital==""):
        break
    i=i+1
    n=n-1

print(len(lista))
print(lista)