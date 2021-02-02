
print("Comparación de 3 números \n")

one = int(input("Introduce el primer número:"))
two = int(input("Introduce el segundo número:"))
three = int(input("Introduce el tercer número:"))

if one > two and one > three:
    print("El número ", one, " es el número más grande de los tres.")
else:
    if two > three:
        print("El número ", two, " es el número más grande de los tres.")
    else:
        print("El número ", three, " es el número más grande de los tres.")