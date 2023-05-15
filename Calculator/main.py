from art import logo

# addition
def add(n1, n2):
    return n1 + n2


# substraction
def substract(n1, n2):
    return n1 - n2


# multiply
def multification(n1, n2):
    return n1 * n2


# division
def division(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": substract,
              "*": multification,
              "/": division
              }


def calculator():
    print(logo)
    num1 = float(input("Enter the first number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation = input("Pick an operation: ")
        num2 = float(input("Enter the next number: "))

        function = operations[operation]
        result = function(n1=num1, n2=num2)
        print(f"{num1} {operation} {num2} = {result}")

        next_operation = input(f"Type 'Y' to continue calculating with {result}, or Type 'n' to exit. ").lower()
        if next_operation == "y":
            num1 = result
        elif next_operation == "n":
            should_continue = False
            calculator()
        else:
            should_continue = False


calculator()
