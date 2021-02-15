# Automates Fibonacci's sequence to number 1597.
firstNumber, secondNumber = 0, 1

while secondNumber <= 1597:

    print(firstNumber, secondNumber, end=" ")
    firstNumber = firstNumber + secondNumber
    secondNumber = firstNumber + secondNumber

print("Software developed by Nicolás Sterzer")