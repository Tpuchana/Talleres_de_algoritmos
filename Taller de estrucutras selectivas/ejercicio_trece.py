mes=int(input("Ingrese su mes de nacimiento "))
dia=int(input("ingrese su día de nacimiento "))

if mes==11 and 22<=dia<=30 or mes==12 and dia<21:
    print(f"Usted es sagitario")
elif mes==12 and 22<=dia<=30 or mes==1 and dia<20:
    print(f"Usted es capricornio")
elif mes==1 and 21<=dia<=30 or mes==2 and dia<19:
    print(f"Usted es acuario")
elif mes==2 and 20<=dia<=30 or mes==3 and dia<19:
    print(f"Usted es piscis")
elif mes==3 and 21<=dia<=30 or mes==4 and dia<20:
    print(f"Usted es aries")
elif mes==4 and 21<=dia<=30 or mes==5 and dia<21:
    print(f"Usted es tauro")
elif mes==5 and 22<=dia<=30 or mes==6 and dia<21:
    print(f"Usted es geminis")
elif mes==6 and 22<=dia<=30 or mes==7 and dia<22:
    print(f"Usted es cancer")
elif mes==7 and 23<=dia<=30 or mes==8 and dia<23:
    print(f"Usted es leo")
elif mes==8 and 24<=dia<=30 or mes==9 and dia<22:
    print(f"Usted es virgo")
elif mes==9 and 23<=dia<=30 or mes==10 and dia<22:
    print(f"Usted es libra")
if mes==10 and 23<=dia<=30 or mes==11 and dia<21:
    print(f"Usted es escorpio")

