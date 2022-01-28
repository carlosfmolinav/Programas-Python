import random

#variables
ALFABETO = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def game(letra):
    print ("Bienvenido al juego de adivinar la letra\nTienes 5 intentos para adivinarla!!\U0001F600\n")
    contador = 1
    while contador <= 5:
        contador+=1
        test = input("Por favor digita la letra que crees que es: ")
        if letra == test:
            print ("\U0001F929 Eres increible, has adivinado la letra: " + letra + "\U0001F929")
            break
        else:
            if contador <= 5:
                print ("Tienes un intento menos \U0001F605 ... Solo te quedan: " + str(6-contador) + "\n")
                continue
            print("El juego ha finalizado, no encontraste la respuesta! \U0001F636 \n")

def run():
    letra = random.choice(ALFABETO)
    game(letra)

if __name__ == "__main__":
    run()