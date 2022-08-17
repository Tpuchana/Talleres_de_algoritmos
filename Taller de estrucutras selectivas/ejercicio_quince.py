edad=float(input("Indique su edad. (en decimales si es en meses) "))
nh=float(input("Introduzca el número de hemoglobina en la sangre "))
sexo=str(input("Indique su sexo "))

if (0<edad<=0.1 and 13>=nh<=26) and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif 1<edad<=0.6 and 10>=nh<=18 and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif 0.6<edad<=1 and 11>=nh<=15 and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif 1<edad<=5 and 11.5>=nh<=15 and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif 5<edad<=10 and 12.6>=nh<=15.5 and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif 10<edad<=14 and 13>=nh<=15.5 and sexo=="mujer" or sexo=="hombre":
    print("Tiene un nivel normal de hemoglobina")
elif edad>15 and 12>=nh<=16 and sexo=="mujer" :
    print("Tiene un nivel normal de hemoglobina")
elif edad>15 and 14>=nh<=18 and sexo== "hombre":
    print("Tiene un nivel normal de hemoglobina")


elif nh<10:
    print("Usted padece de anemia")