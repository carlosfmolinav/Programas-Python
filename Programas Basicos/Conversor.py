#Este es un conversor de monedas de quetzales a d贸lares o de d贸lares a quetzales
def conversor(consulta, tasa_cambio, moneda1, moneda2):
    cant_convertir = float(input(consulta))
    respuesta = round(cant_convertir / tasa_cambio,2)
    return str(cant_convertir) + " " + moneda1 + " equivalen, en este momento, a " + str(respuesta) + " " + moneda2

menu=("""
Bienvenido al conversor de monedas 馃挷
Por favor, seleccione la opci贸n que desea:
[1] Convertir quetzales a d贸lares
[2] Convertir d贸lares a quetzales
""") #con la tecla windows + punto, me salen las opciones de los emojis.

conversor_dq_qd = input(menu)

if conversor_dq_qd == "1":
    respuesta = conversor("Por favor ingresa la cantidad de quetzales que deseas convertir a d贸lares: ",7.71,"quetzales","d贸lares")
    print(respuesta)
elif conversor_dq_qd == "2":
    respuesta = conversor("Por favor ingresa la cantidad de d贸lares que deseas convertir a quetzales: ",0.13,"d贸lares","quetzales")
    print(respuesta)
else:
    print("Ingrese una opci贸n de la lista")