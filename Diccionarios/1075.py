a=int(input())
b=int(input())
x=max(a,b)
y=min(a,b)
suma=0
for i in range(x,y+1):
  if(i%13!=0):
    suma=suma+i
print(suma)