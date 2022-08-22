from ast import Str


encuestados=[]
consumidores=[]
edad=[]
bebidas=[]
sexo=[]

cantidadEncuestados=int(input("Ingrese el numero de encuestados "))
e=0
i=0
contSi=0
sexoM=0
sexoF=0
mayorde=0
menorde=0
while (i<cantidadEncuestados):
    e=i+1
    encuestados.append(e)
    consE=str(input("Consume licor? "))
    consumidores.append(consE)
    if (consE==("no")):
        edadE=int(input("Que edad tiene? "))
        edad.append(edadE)
        if edadE>18:
            mayorde=mayorde+1
        if edadE<18:
            menorde=menorde+1



        sexoE=Str(input("Su sexo? "))
        sexo.append(sexoE)
        if sexoE == "M":
            sexoM=sexoM+1
        if sexoE == "F":
            sexoM=sexoF+1
         
    if (consE=="si"):
        contSi=contSi+1
        edadE=int(input("Que edad tiene? "))
        edad.append(edadE)
        if edadE>18:
            mayorde=mayorde+1
        if edadE<18:
            menorde=menorde+1
        bebidasE=int(input("Que tipo de licor le gusta? "))
        if bebidasE == 1:
         bebidas.append('Aguardiente')
        if bebidasE == 2:
         bebidas.append('Ron')
        if bebidasE == 3:
          bebidas.append('Cerveza')
        if bebidasE == 4:
          bebidas.append('Tequila')
        if bebidasE == 5:
          bebidas.append('Wisky')
        if bebidasE == 6:
          bebidas.append('Otros')         
        sexoE=Str(input("Su sexo? "))
        sexo.append(sexoE) 
        if sexoE == "M":
            sexoM=sexoM+1
        if sexoE == "F":
            sexoM=sexoF+1  
    i=i+1

print(f"El total de consumidores es de: {contSi}")
print(f"El total de mujeres menores de edad es de {sexoF-mayorde}")







    
    



