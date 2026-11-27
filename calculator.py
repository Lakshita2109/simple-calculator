"""Simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return round(a / b, 4)


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    print("Simple Calculator")
    a = float(input("First number: "))
    op = input("Operation (+ - * /): ").strip()
    b = float(input("Second number: "))
    if op not in OPERATIONS:
        print("Unknown operation:", op)
        return
    try:
        print("Result:", OPERATIONS[op](a, b))
    except ValueError as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
