diccionario={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 'Maite': 5} 
Lista=[]
for i in diccionario:
    if (not(diccionario[i] in Lista)) :
     Lista.append(diccionario[i])
    
print(Lista)