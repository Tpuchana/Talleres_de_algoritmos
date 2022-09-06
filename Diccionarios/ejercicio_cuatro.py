lista_nombres=[]
lista_notas=[]
contador=0
contadorperder=0
contadorganar=0
i=1



for i in range(1, 10+1):
  nombre=input("Ingrese el nombre del estudiante: ")
  nota=int(input("Ingrese nota del estudiante: "))
  lista_nombres.append(nombre)
  lista_notas.append(nota)
  contador=contador+nota
  if nota<60:
    contadorperder=contadorperder+1
  else:
    contadorganar=contadorganar+1


diccionario= {
    "1":{

    "nombreestudiante": f"{lista_nombres[0]}",
    "notaestudiante": f"{lista_notas[0]}"
    },
    "2":{

    "nombreestudiante": f"{lista_nombres[1]}",
    "notaestudiante": f"{lista_notas[1]}"
    },
    "3":{

    "nombreestudiante": f"{lista_nombres[2]}",
    "notaestudiante": f"{lista_notas[2]}"
    },
    "4":{

    "nombreestudiante": f"{lista_nombres[3]}",
    "notaestudiante": f"{lista_notas[3]}"
    },
    "5":{

    "nombreestudiante": f"{lista_nombres[4]}",
    "notaestudiante": f"{lista_notas[4]}"
    },
    "6":{

    "nombreestudiante": f"{lista_nombres[5]}",
    "notaestudiante": f"{lista_notas[5]}"
    },
     "7":{

    "nombreestudiante": f"{lista_nombres[6]}",
    "notaestudiante": f"{lista_notas[6]}"
    },
     "8":{

    "nombreestudiante": f"{lista_nombres[7]}",
    "notaestudiante": f"{lista_notas[7]}"
    },
     "9":{

    "nombreestudiante": f"{lista_nombres[8]}",
    "notaestudiante": f"{lista_notas[8]}"
    },
     "10":{

    "nombreestudiante": f"{lista_nombres[9]}",
    "notaestudiante": f"{lista_notas[9]}"
    }
}

prom=contador/10
print(f"La cantdidad de estudiantes que perdieron fue de: {contadorperder}, los que pasaron fueron: {contadorganar}, el promedio de notas fue de : {prom}")

