#Función de verificación de si es palíndromo
def fpalindromo(frase):
    frase = frase.replace(" ","")
    frase = frase.lower()
    frase_invertida = frase[::-1]
    if frase == frase_invertida:
        return True
    else:
        return False


#Función principal
def run():
    frase = input("Escribe una palabra o una frase: ")
    es_palindromo = fpalindromo(frase)
    if es_palindromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")


#Entrypoint / punto de entrada
if __name__ == "__main__":
    run()
