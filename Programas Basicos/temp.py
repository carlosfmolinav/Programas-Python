def run():
    anios = input("Por favor ingrese su edad: ")
    anios = anios.replace('años','')
    anios = int(anios)
    print(f'Su edad es: {anios} años')
    print(f'{"Hip "*3}Hurra')
    cadena = input("Por favor digite una palabra: ")
    for letra in cadena[::-1]:
        print(letra)

    car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    x = car.items()
    print(x) #before the change
    car["year"] = 2020
    print(x) #after the change
    print(x["model"])

if __name__ == "__main__":
    run()