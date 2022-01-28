#Algoritmo 1: Enumeración Exhaustiva (Ej. búsqueda de raíz cuadrada)
objetivo = int(input("Por favor digite el número del que desea la raíz cuadrada: "))
respuesta = 0

while respuesta**2 < objetivo:
    respuesta +=1

if respuesta**2==objetivo:
    print(f"La raíz cuadrada de {objetivo} es: {respuesta}")
else:
    print(f"El número {objetivo} no tiene una raíz cuadrada")