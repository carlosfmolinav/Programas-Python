import random

def genpas():
    #Creación de listas bases
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    #Creación de una nueva lista con todas las anteriores
    universe = MAYUS + MINUS + NUMS + CHARS

    lpass = []
    for i in range(0,15):
        caracter = random.choice(universe)
        lpass.append(caracter)
    #Convertimos la contraseña tipo lista a string
    finalpass = "".join(lpass)
    return finalpass

def run():
    passw = genpas()
    print('Tu nueva contraseña es: ' + passw)


if __name__ == '__main__':
    run()