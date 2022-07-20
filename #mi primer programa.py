#mi primer programa
print("calculo de promedio de 5 notas")
lista4 = []
suma = 0
for i in range(1, 6):
    n = float(input(f'ingrese la nota {i}:  '))
    while n < 0 or n > 10:
            n = float(input(f'ingrese la nota {i}:  '))
    lista4.append(n)
    suma = suma + n
    prom = suma / 5
print("notas:  ",end=" ")
for  n in lista4:
    print(n, " ",end= " ")
print()
print("el promedio es: ",prom)
print("la nota alta es " , max(lista4) , "la nota baja es ", min(lista4))

