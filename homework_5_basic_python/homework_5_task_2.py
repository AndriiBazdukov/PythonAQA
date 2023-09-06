class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


attempts = 3

while attempts > 0:
    formula = input(f"Example \"2 * 5\" \nYou have {attempts} attempts left:\nEnter values: ")
    attempts -= 1

    try:
        elements = formula.split()
        if len(elements) != 3:
            raise FormulaError("Invalid formula.")

        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])

        if operator not in ('*', '/'):
            raise WrongOperatorError("Unsupported operator. Please use '*' or '/'.")

        if operator == '/' and num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")

        if operator == '*':
            result = num1 * num2
        else:
            result = num1 / num2

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except WrongOperatorError as e:
        print(e)
    except FormulaError as e:
        print(e)
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    else:
        print(f"Result: {result:.2f}")
        break
else:
    print("Exceeded maximum attempts.")
