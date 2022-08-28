listatemp=[]
n=int(input("Introduzca el número de temperaturas "))
i=1
t=0

while (n>0):
    temp= float(input(f"Introduza la temperatura#{i} "))
    listatemp.append(temp)
    if 20>(listatemp[])>15:
        t=t+1
        print(f"{listatemp}, {t}")
    i=i+1
    n=n-1

