edades = [18, 11, 34, 63, 20, 28, 45, 22, 9]
print(f"original: {edades}")

edades[8]=19
edades[2]=24

print(f"con números cambiados: {edades}")

nuevosnumeros= 21,32,16
edades.append(nuevosnumeros)
print(f"con los nuevos números: {edades}")

del edades[0]
del edades[6]

print(f"con los elementos removidos: {edades}")