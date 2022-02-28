
def primera_letra(lista_de_palabras):
    primeras_letras = []
    for palabra in lista_de_palabras:
        try:
            assert type(palabra) == str, f'{palabra} no es string'
            assert len(palabra) > 0, f'No se permite string vacio'
            primeras_letras.append(palabra[0])
        except AssertionError as e:
            print(e)

    return primeras_letras

def run():
    #lista_de_palabras = ["carlos","francisco","molina","villatoro"]
    lista_de_palabras = ["",3]
    print(primera_letra(lista_de_palabras))

if __name__ == "__main__":
    run()