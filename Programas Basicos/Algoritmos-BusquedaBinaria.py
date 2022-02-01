#epsilon: margen de error
epsilon = 0.001
numeroencontrar = int(input("Por favor digite el número al que desea encontrar su raíz cuadrada: "))

#Utilizaremos dos variables: limite inferior y limite superior
limiteinterior = 0.00
limitesuperior = max(1.0,numeroencontrar)
respuesta = (limiteinterior+limitesuperior)/2

while (abs(respuesta**2 - numeroencontrar) >= epsilon):
    if( respuesta**2  > numeroencontrar ):
        limitesuperior = respuesta
    else:
        limiteinterior = respuesta
    #tratamos de encontrar la respuesta
    respuesta = (limiteinterior+limitesuperior)/2

print(f"La raíz cuadrada de {numeroencontrar} es: {respuesta}")