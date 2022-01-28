def factorial(n):
    #Utilizamos recursividad en función
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

def esPrimo(num):
    #Aplicamos el teorema de Wilson
    fact = factorial(num-1)
    print ("El número es primo") if ((fact+1) % num == 0) else print ("El número no es primo")

def run():
    print("Bienvenido, este programa te permitirá saber si un número es primo.\n")
    num = int(input("Por favor digita el número: "))
    if num == 1:
        print("El número 1 no es un número primo.\n")
    elif num == 2:
        print("Felicidades, el 2 es el primer número primo.\n")
    else:
        esPrimo(num)

if __name__ == "__main__":
    run()