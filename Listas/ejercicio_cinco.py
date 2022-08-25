lista=[]
n=int(input("Introduzca el número de países "))
i=1

while (n>0):
    paisyc= tuple(input(f"Introduza un país y su capital"))
    lista.append(paisyc)
    i=i+1
    n=n-1

print(lista)