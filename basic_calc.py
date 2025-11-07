def calculator():
    """A simple calculator that takes two numbers and an operator"""
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero!")
                return
            result = num1 / num2
        else:
            print("Invalid operator!")
            return

        print(f"Result: {num1} {operator} {num2} = {result}")

    except ValueError:
        print("Please enter valid numbers!")
calculator()