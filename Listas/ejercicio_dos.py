edades = [18, 11, 34, 63, 20, 28, 45, 22, 9]

print(f"La lista es: {edades}")
print(f"El segundo elemento es: {edades[1]}")
print(f"El último elemento es: {edades[-1]}")
print(f"El último elemento es: {edades[4]}")

primeros= (edades[0], edades[1], edades[2], edades[3], edades[4], edades[5] )
print(f"Los primeros seis elementos son: {primeros}")
ultimos= (edades[6], edades[7], edades[8])
print(f"Los últimos tres elementos son: {ultimos}")
primeros2= (edades[1], edades[2], edades[3], edades[4], edades[5])
print(f"Los primeros seis elementos exceptuando el primero son: {primeros2}")
ultimos2= (edades[6], edades[7])
print(f"Los ultimos tres elementos exceptuando el último son: {ultimos2}")