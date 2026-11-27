"""Simple command-line calculator."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def main():
    print("Simple Calculator")
    a = float(input("First number: "))
    op = input("Operation (+ - * /): ").strip()
    b = float(input("Second number: "))
    if op not in OPERATIONS:
        print("Unknown operation:", op)
        return
    print("Result:", OPERATIONS[op](a, b))


if __name__ == "__main__":
    main()
