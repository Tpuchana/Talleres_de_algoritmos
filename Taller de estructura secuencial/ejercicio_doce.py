t_1=float(input("introduzca su primera nota de matematicas"))
t_2=float(input("introduzca su segunda nota de matematicas"))
t_3=float(input("introduzca su tercera nota de matematicas"))
e_1=float(input("introduzca su nota de examen de matematicas"))
tt_1=float(input("introduzca su primera nota de fisica"))
tt_2=float(input("introduzca su segunda nota de fisica"))
e_2=float(input("introduzca su nota de examen de fisica"))
ttt_1=float(input("introduzca su tercera nota de quimica"))
ttt_2=float(input("introduzca su segunda nota de quimica"))
ttt_3=float(input("introduzca su tercera nota de quimica"))
e_3=float(input("introduzca su nota de examen de quimica"))

ma=((((t_1+t_2+t_3)/3)*0.10)+((e_1)*0.90))
fi=((((tt_1+tt_2)/2)*0.20)+((e_2)*0.80))
qui=((((ttt_1+ttt_2+ttt_3)/3)*0.15)+((e_3)*0.85))
fin=(ma+fi+qui)/3

print(f"Matemáticas {ma} , Física {fi} , Química {qui}, el promedio del semestre es: {fin}")
