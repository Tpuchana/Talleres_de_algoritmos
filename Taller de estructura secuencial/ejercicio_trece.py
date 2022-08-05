bci=int(input("¿Con cuántos billetes de 50000 cuenta?"))
bve=int(input("¿Con cuántos billetes de 20000 cuenta?"))
bdi=int(input("¿Con cuántos billetes de 10000 cuenta?"))
bcin=int(input("¿Con cuántos billetes de 5000 cuenta?"))
bdo=int(input("¿Con cuántos billetes de 2000 cuenta?"))
bmi=int(input("¿Con cuántos billetes de 1000 cuenta?"))
bqui=int(input("¿Con cuántos billetes de 500 cuenta?"))
bcie=int(input("¿Con cuántos billetes de 100 cuenta?"))

total=((bci*50000)+(bve*20000)+(bdi*10000)+(bcin*5000)+(bdo*2000)+(bmi*1000)+(bqui*500)+(bcie*100))

print(f"Hay un total de {total} pesos")