# cargar en un dicccionario los datos de data.txt que tiene 
# el formato: fecha, importe, categoria
# sin usar import csv

gastos = []
with open('data.csv') as data:
    for line in data:
        gastos.append(line)
        print(line, end='')

print(gastos)


## lista bde numeros primos hasta 100
primos = []
for i in range(2, 101):
    cota = int(i**0.5)
    for j in range(2, cota + 1):
        if i % j == 0:
            break
    else:
        primos.append(i)

print("Los primeros 100 numeros primos son:")
print(primos)

## dame usando lista por compresión los numeros impares hasta 100
impares = [i for i in range(1, 101) if i % 2 != 0]
print(impares)