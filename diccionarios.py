def run():
    mi_diccionario = {
        "id": 1,
        "nombre": "carlos",
        "apellido": "molina",
        "edad": 37
    }
    print(mi_diccionario)
    
    for key in mi_diccionario.keys():
        print(key)

    for valor in mi_diccionario.values():
        print(valor)

    for key, valor in mi_diccionario.items():
        print("La llave es: " + key + " y su valor es:" + str(valor))

if __name__ == "__main__":
    run()