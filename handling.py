import logging

# Create log file
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Custom Exception
class NegativeNumberError(Exception):
    pass


def divide_numbers(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError as e:
        logging.error(e)
        print("Error: Cannot divide by zero")


def square_root(num):
    try:
        if num < 0:
            raise NegativeNumberError(
                "Negative number not allowed for square root")

        return num ** 0.5

    except NegativeNumberError as e:
        logging.error(e)
        print(e)


def list_access():
    try:
        numbers = [10, 20, 30]
        print(numbers[5])

    except IndexError as e:
        logging.error(e)
        print("Invalid List Index")


try:
    print("Division Result:")
    print(divide_numbers(10, 0))

    print("\nSquare Root:")
    print(square_root(-25))

    print("\nList Access:")
    list_access()

except Exception as e:
    logging.error(e)

finally:
    print("\nProgram Executed Successfully")
