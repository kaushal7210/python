def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    num1 = float(input("What's the first number?\n"))

    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation.\n")
        num2 = float(input("What's the next number?\n"))
        calculation_symbol = operations[operation_symbol]
        answer = calculation_symbol(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        for_next = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or "
                         f"type 'x' to exit the calculation.\n")
        if for_next == "y":
            num1 = answer

        elif for_next == "x":
            should_continue = False

        else:
            should_continue = False
            calculator()


calculator()
