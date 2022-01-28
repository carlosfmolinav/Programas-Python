contador = 1
print(contador)
while contador < 10:
    contador+=1
    print(contador)

#range = rango de 0 hasta el número establecido, es una función
a=range(10)
print(a)

for contadorf in range(1,11):
    print(contadorf)

print("Ejercicio con While: Break and Continue")

edad = int(input("Por favor ingresa tu edad: "))
contadorbc = 0
print("Los números divisibles entre 5 menores a tu edad son")
while contadorbc < 100:
    contadorbc += 1
    # Si es divisible entre 5 lo imprimo
    if contadorbc % 5 == 0:
        print (contadorbc)
        continue
    if contadorbc == edad:
        break
        