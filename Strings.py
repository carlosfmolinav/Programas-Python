#Strings
print("Original text:")
txt = "we are the so-called \"Vikings\" from the North. \n \f \\ "
print(txt)
txt = "we are the so-called \"Vikings\" from the North. {}"
print("Invertir cadenas:")
txt_inv = txt[::-1]
print(txt_inv)

#String Methods
print("Capitalize")
print(txt.capitalize())
print("Casefold")
print(txt.casefold())
print("Center")
print(txt.center(60))
print("Count")
print(txt.count("a"))
print("Endcode")
print(txt.encode())
print("Endswith")
print(txt.endswith(" "))
print("Expandtabs")
print(txt.expandtabs())
print("Find")
print(txt.find("the"))
print("Index")
print(txt.index("the"))