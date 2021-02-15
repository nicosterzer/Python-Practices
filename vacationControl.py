print("* Vacation control system for companies \n")

# Introduces key from 1 - 3.
employeeName = input("Introduce employee's name: ")
departmentKey = int(input("Introduce Department Key (1 - 3): "))
employeeLongevity = float(input("Introduce years of employee: "))

if departmentKey == 1:

    if  employeeLongevity == 1 and employeeLongevity < 2:
        print("Employee ", employeeName, " has 6 days of vacation.")
    elif employeeLongevity >= 2 and employeeLongevity <= 6:
        print("Employee ", employeeName, " has 14 days of vacation.")
    elif employeeLongevity >= 7:
        print("Employee ", employeeName, " has 20 days of vacation.")
    else:
        print("Employee ", employeeName, " has no vacation days.")

elif departmentKey == 2:

    if employeeLongevity == 1 and employeeLongevity < 2:
        print("Employee ", employeeName, "has 7 days of vacation.")
    elif employeeLongevity >= 2 and employeeLongevity <= 6:
        print("Employee ", employeeName, " has 15 days of vacation.")
    elif employeeLongevity >= 7:
        print("Employee ", employeeName, " has 22 days of vacation.")
    else:
        print("Employee ", employeeName, " has no vacation days.")

elif departmentKey == 3:

    if employeeLongevity == 1 and employeeLongevity < 2:
        print("Employee ", employeeName, " has 10 days of vacation.")
    elif employeeLongevity >= 2 and employeeLongevity <= 6:
        print("Employee ", employeeName, " has 20 days of vacation.")
    elif employeeLongevity >= 7:
        print("Employee ", employeeName, " has 30 days of vacation.")
    else:
        print("Employee ", employeeName, " has no vacation days.")

else:
    print("Department key is non existant, try again.")
