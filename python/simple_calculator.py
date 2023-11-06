# Import required modules
from os import path
from logging import basicConfig, error, INFO, info, getLogger, warning

# Get the current path of the script
current_path = path.dirname(path.abspath(__file__))
log_file = path.join(current_path, 'calculator.log')

# Configure logging
basicConfig(
    filename=log_file,
    level=INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = getLogger(__name__)


def main():
    """
    Main function to initiate and control the calculator program.
    """
    # Define the valid calculation types
    calculation_types = ['add', 'subtract', 'multiply', 'divide', 'quit']

    while True:
        # Initialize variables
        num1, num2, result, calc_type = None, None, None, None

        # Get the user's choice of calculation
        while calc_type not in calculation_types:
            calc_type = input("Pick your calculation ['add', 'subtract', 'multiply', 'divide', 'quit']: ").lower()

            if calc_type not in calculation_types:
                warning("Please input a valid option e.g., 'add'.")
            elif calc_type == 'quit':
                info("Exited the program.")
                exit()

        # Get the user's input for the two numbers
        while not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
            try:
                num1 = float(input("First number: "))
                num2 = float(input(f"{calc_type.capitalize()} the second number: "))
            except ValueError:
                error("Invalid input. Please enter a number.")
                print("Invalid input. Please enter a number.")

        # Perform the selected calculation
        if calc_type == 'add':
            result = add(num1, num2)
        elif calc_type == 'subtract':
            result = subtract(num1, num2)
        elif calc_type == 'multiply':
            result = multiply(num1, num2)
        elif calc_type == 'divide':
            result = divide(num1, num2)

        # Display the result
        try:
            if not result.is_integer():
                result = "{:.2f}".format(result)
        except AttributeError:
            error(f"An AttributeError occurred due to a ZeroDivisionError. Result: {result}")
            print(f"An AttributeError occurred due to a ZeroDivisionError. Result: {result}")
            print()
        else:
            info(f"Your calculation result: {result}")
            print(f"Your calculation result: {result}")
            print()


# Define functions for various calculations
def add(num1, num2):
    """
    Perform addition of two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The result of the addition.
    """
    result = num1 + num2
    info(f"{num1} added to {num2} is {result}")
    return result


def subtract(num1, num2):
    """
    Perform subtraction of two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The result of the subtraction.
    """
    result = num1 - num2
    info(f"{num1} minus {num2} is {result}")
    return result


def multiply(num1, num2):
    """
    Perform multiplication of two numbers.

    :param num1: The first number.
    :param num2: The second number.
    :return: The result of the multiplication.
    """
    result = num1 * num2
    info(f"{num1} multiplied by {num2} is {result}")
    return result


def divide(num1, num2):
    """
    Perform division of two numbers.

    :param num1: The dividend.
    :param num2: The divisor.
    :return: The result of the division.
    """
    try:
        result = num1 / num2
        info(f"{num1} divided by {num2} is {result}")
        return result
    except ZeroDivisionError:
        error("Cannot divide by zero!")
        return "Cannot divide by zero!"


if __name__ == "__main__":
    main()  # Start the calculator program
