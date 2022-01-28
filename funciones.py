def nota(mensaje):
    print("")
    print("Buen día, ¿cómo estas?")
    print(mensaje)
    print("Recuerda llenar la encuestra de satisfacción, nos será de mucha ayuda")
    print("")

opcion = input("""
Por favor selecciona una opción:
1- Deberías de leer "En un lugar llamado tierra..."
2- Siempre es buen momento para disfrutar de "Cien años de soledad"
3- Harry Potter ¿por qué no?
""")

if opcion == "1":
    nota("Excelente opción, recuerda que En un lugar llamado Tierra es un trilogia")
elif opcion == "2":
    nota("Cien años de soledad, es sin lugar a dudas un libro para una tarde de lluvia y café con pan")
elif opcion == "3":
    nota("Great! El septimo libro es mi favorito")
else:
    print("Por favor selecciona una opción de las disponibles")