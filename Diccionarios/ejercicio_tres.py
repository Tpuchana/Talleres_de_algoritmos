usuarios = { 
 "iperurena": { 
 "nombre": "Iñaki", 
 "apellido": "Perurena", 
 "password": "123123" 
 }, 
 "fmuguruza": { 
 "nombre": "Fermín", 
 "apellido": "Muguruza", 
 "password": "654321" 
 }, 
 "aolaizola": { 
 "nombre": "Aimar", 
 "apellido": "Olaizola", 
 "password": "123456"  } 
 } 

Usuario = input("Escriba su usuario: ")
Contraseña = input("Escriba su contraseña: ")

if Usuario in usuarios and Contraseña == usuarios[Usuario]["password"]:
     print(f"Bienvenido {Usuario}")
else:
    print("Usuario o contraseña incorrecta")

