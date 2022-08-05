aus=float(input("Escriba un monto en chelines austriacos:"))
gre=float(input("Escriba un monto en dracmas griegos:"))
esp=float(input("Escriba un monto en pesetas:"))

con1=(aus*956871)/100
con2=((gre*88607)/100)/(20110)
con3=(esp/122499)
con4=(esp*100)/9289

print(f"La conversón de {aus} chelines australianos a pesetas es: {con1} pesetas , la conversión de {gre} dracmas griegos a francos franceses es de {con2} , la conversión de {esp} pesetas españolas a dolares es de: {con3} dolares , la conversión de {esp} pesetas españolas a liras italianas es de: {con4} liras italianas ")
