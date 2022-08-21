gas = 0
alc = 0
di = 0

while True:
    dato = int(input(""))
    if dato == 1:
        alc += 1
    elif dato == 2:
        gas += 1
    elif dato == 3:
        di += 1
    elif dato == 4:
        break
print('MUITO OBRIGADO')
print(f'Alcool: {alc}')
print(f'Gasolina: {gas}')
print(f'Diesel: {di}')