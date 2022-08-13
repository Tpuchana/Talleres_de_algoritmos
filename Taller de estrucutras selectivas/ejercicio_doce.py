valor=int(input("Ingrese la cantidad en pesos"))

if valor>100000:
    print((valor//100000), " billetes de 100.000 pesos")
if valor>=50000<100000:
    print(((valor%100000)//50000), " billetes de 50.000 pesos")
if valor>=20000<50000:
    print((valor%50000//20000), " billetes de 20.000 pesos")
if valor>=10000<20000:
    print((valor%20000//10000), " billetes de 10.000 pesos")
if valor>=5000<10000:
    print(((valor%10000)//5000), " billetes de 5.000 pesos")
if valor>=2000<5000:
    print((valor%5000//2000), " billetes de 2.000 pesos")
if valor>=1000<2000:
    print(((valor%5000)//1000), " billetes de 1.000 pesos")
if valor>=500<1000:
    print((valor%1000//500), " monedas de 500 pesos")
if valor>=200<500:
    print(((valor%500)//200), " monedas de 200 pesos")
if valor>=100<200:
    print((valor%200//100), " monedas de 100 pesos")
if valor>=50<100:
    print(((valor%100)//50), " monedas de 50 pesos")