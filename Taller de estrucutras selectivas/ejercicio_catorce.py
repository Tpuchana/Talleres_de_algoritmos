lectan=int(input("Introduzca la lectura anterior de consumo eléctrico"))
lectac=int(input("Introduzca la lectura actual del consumo eléctrico"))

lectura=(lectac-lectan)

if 0<lectura<=100:
    lec1=(lectura*4600)
    print(f"El valor a pagar es de {lec1} pesos")

elif 101<=lectura<=300:
    lec2=(lectura*8000)
    print(f"El valor a pagar es de {lec2} pesos")

elif 301<=lectura<=500:
    lec3=(lectura*100000)
    print(f"El valor a pagar es de {lec3} pesos")

elif lectura>=501:
    lec4=(lectura*120000)
    print(f"El valor a pagar es de {lec4} pesos")
