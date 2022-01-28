def calculoPotenciaDos(limite):
    num = 1
    dos = 2
    potencia = 0
    while num <= limite:
        print(num)
        potencia += 1
        num=dos**potencia

#Función principal
def run():
    #Para definir constantes en lugar de variables, utiliza mayúsculas
    LIMITE = 1000
    calculoPotenciaDos(LIMITE)

#Entrypoint / punto de entrada
if __name__ == "__main__":
    run()