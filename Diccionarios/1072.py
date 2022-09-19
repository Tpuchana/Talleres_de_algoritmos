n=int(input(""))
dentro=0
fuera=0
c=0

while True:
    c=c+1
    if(n==0):
        break
numero=int(input(""))
if(numero>=10 and numero<=20):
    dentro==dentro+1
else:
    fuera==fuera+1
print(f"{dentro} in")
print(f"{fuera} out")