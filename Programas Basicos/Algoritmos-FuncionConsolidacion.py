def enumExha():
    objetivo = int(input("Por favor digite el número del que desea la raíz cuadrada: "))
    respuesta = 0

    while respuesta**2 < objetivo:
        respuesta +=1

    if respuesta**2==objetivo:
        print(f"La raíz cuadrada de {objetivo} es: {respuesta}")
    else:
        print(f"El número {objetivo} no tiene una raíz cuadrada")

def aproxSolu():
    epsilon = 0.001
    paso = epsilon**2
    respuesta = 0.00
    numeroencontrar = int(input("Por favor digite el número al que desea encontrar su raíz cuadrada: "))
    if numeroencontrar <= 0:
        print("Por favor digite un número positivo")
    else:
        while (abs(respuesta**2 - numeroencontrar) >= epsilon):
            respuesta += paso
        
        if (respuesta**2 - numeroencontrar) >= epsilon:
            print(f"El número {numeroencontrar} no tiene raíz cuadra exacta.")
        else:
            print(f"La raíz cuadrada de {numeroencontrar}, considerando un epsilon de {epsilon}, es: {respuesta}")
            print(f"Tambien puedo aproximar la respuesta {round(respuesta,0)}")

def busBina():
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

def validacionParametro(parametro):
    if parametro < 1 or parametro > 3:
        return False
    else:
        if parametro == 1:
            enumExha()
            return True
        elif parametro == 2:
            aproxSolu()
            return True
        else:
            busBina()
            return True

def run():
    print("\nBienvenido al proceso para encontrar el número primo de un número.\nPara ello hemos decidido utilizar algoritmos para determinar la mejor solución.\n")
    parametro = input("Por favor selecciona la opción que desees utilizar:\n 1)Enumeración Exhaustiva\n 2)Aproximación de Soluciones\n 3)Búsqueda Binaria\n\n:")
    if validacionParametro(int(parametro)) == False:
        pregunta = input("No has seleccionado una opción valida. ¿Quieres intertarlo nuevamente? Si/No\n:")
        if pregunta.upper() == "SI":
            run()
        else:
            print("Lamentamos que no quieras participar, gracias por tu tiempo.")
    else:
        pregunta = input("¿Quieres intertarlo nuevamente? Si/No\n:")
        if pregunta.upper() == "SI":
            run()
        else:
            print("Lamentamos que no quieras participar, gracias por tu tiempo.")

if __name__ == "__main__":
    run()