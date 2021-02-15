# Introduction to program.
print("3 number comparison \n")

# Asks to insert desired numbers.
one = int(input("Introduce first number:"))
two = int(input("Introduce second number:"))
three = int(input("Introduce third number:"))

# Conditional statements to determine which number is bigger.
if one > two and one > three:

    print("Number ", one, " it's the bigger of them all")

elif two > three:

        print("Number", two, " it's the bigger of them all")

else:

    print("Number ", three, " it's the bigger of them all")