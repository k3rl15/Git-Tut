def main():
    types = ['add', 'minus', 'multiply', 'divide']
    num1, num2, result, calc_type = None, None, None, None
    while calc_type not in types:
        calc_type = input("Pick you calcultion['add', 'minus', 'multiply', 'divide']: ").lower()

    while not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        try:
            num1 = float(input("First number: "))
            num2 = float(input(f"{calc_type.capitalize()} second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")

    if calc_type == 'add':
        result = add(num1, num2)
    elif calc_type == 'minus':
        result = minus(num1, num2)
    elif calc_type == 'multiply':
        result = multiply(num1, num2)
    elif calc_type == 'divide':
        result = divide(num1, num2)

    if not result.is_integer():
        result = "{:.2f".format(result)

    print(f"Your calculation total: {result}")


def add(num1, num2):
    return num1 + num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    return num1 / num2


if __name__ == "__main__":
    main()
