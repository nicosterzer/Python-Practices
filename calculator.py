# Introduction and options.
print("Calculator\n")
print("* Options menu *")

print("1. Sum")
print("2. Substraction")
print("3. Multiplication ")
print("4. Division")
print("5. Exponent")

# Insert one of the options listed above.
number = int(input("Introduce the desired option:"))

# Conditional statements according to the chosen option.
if number == 1:

    print("Sum \n")
    number = int(input("Introduce first number:"))
    number += int(input("Introduce second number:"))
    print("The result is: ", number)

elif number == 2:

    print("Substraction \n")
    number = int(input("Introduce first number:"))
    number -= int(input("Introduce second number:"))
    print("The result is:", number)

elif number == 3:

    print("Multiplication \n")
    number = int(input("Introduce first number:"))
    number *= int(input("Introduce secondnumber:"))
    print("The result is:", number)

elif number == 4:

    print("Division \n")
    number = float(input("Introduce first number:"))
    number /= float(input("Introduce second number:"))
    print("The result is:", round(number, 2))

elif number == 5:

    print("Exponent \n")
    number = int(input("Introduce first number:"))
    number **= int(input("Introduce second number:"))
    print("The result is:", number)

else:
    
    print("Chosen option is non existant. Try again.")