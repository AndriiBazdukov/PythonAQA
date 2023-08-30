operation = int(input('Menu\n1 - Calculator\n2 - Temperature calculator'
                      '\n3 - Fluid volume and temperature calculator\nPlease choose menu item: '))

if operation == 1:
    first_int = int(input("Please enter firs integer "))
    second_int = int(input("Please enter second integer "))
    operation = input("Please choose operation ")

    if operation == "+":
        print(f"Result: {first_int + second_int}")

    elif operation == "-":
        print(f"Result: {first_int - second_int}")

    elif operation == "/":
        print(f"Result: {first_int / second_int}")

    elif operation == "*":
        print(f"Result: {first_int * second_int}")

    elif operation == "**":
        print(f"Result: {first_int ** second_int}")

    else:
        print("operation sign is incorrect")

if operation == 2:
    temperatureC = float(input("Please enter temperature C "))
    print(f"{temperatureC} C\n{temperatureC * 9 / 5 + 32} F\n{temperatureC + 273.15} K")

if operation == 3:
    volume1 = float(input("Enter the volume of the first liquid: "))
    temperature1 = float(input("Enter the temperature of the first liquid: "))
    volume2 = float(input("Enter the volume of the second liquid: "))
    temperature2 = float(input("Enter the temperature of the second liquid: "))

    total_volume = volume1 + volume2
    print(f"Total volume is: {total_volume}")
    print(f"Temperature: {(volume1 * temperature1 + volume2 * temperature2) / total_volume}")
