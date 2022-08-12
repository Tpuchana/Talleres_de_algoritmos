p=int(input("Escriba el número del valor P "))
q=int(input("Escriba el número del valor q "))

formula=((p**3)+(q**4)-(2*p**2))

if formula > 680:
    print(f"P y Q satisfacen la expresión, el valor fue de {formula}")
else: print(f"P y Q no satisfacen la expresión, el valor fue de {formula}")
