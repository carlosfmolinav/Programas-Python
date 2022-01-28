#Este es un conversor de monedas de quetzales a dólares o de dólares a quetzales
def conversor(consulta, tasa_cambio, moneda1, moneda2):
    cant_convertir = float(input(consulta))
    respuesta = round(cant_convertir / tasa_cambio,2)
    return str(cant_convertir) + " " + moneda1 + " equivalen, en este momento, a " + str(respuesta) + " " + moneda2

menu=("""
Bienvenido al conversor de monedas 💲
Por favor, seleccione la opción que desea:
[1] Convertir quetzales a dólares
[2] Convertir dólares a quetzales
""") #con la tecla windows + punto, me salen las opciones de los emojis.

conversor_dq_qd = input(menu)

if conversor_dq_qd == "1":
    respuesta = conversor("Por favor ingresa la cantidad de quetzales que deseas convertir a dólares: ",7.71,"quetzales","dólares")
    print(respuesta)
elif conversor_dq_qd == "2":
    respuesta = conversor("Por favor ingresa la cantidad de dólares que deseas convertir a quetzales: ",0.13,"dólares","quetzales")
    print(respuesta)
else:
    print("Ingrese una opción de la lista")