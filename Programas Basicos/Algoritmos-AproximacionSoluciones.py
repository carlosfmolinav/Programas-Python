#epsilon: margen de error
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

