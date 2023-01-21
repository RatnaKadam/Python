logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)
# Calculator

# Addition
def add(num1, num2):
    return num1 + num2


# Subtract
def subtract(num1, num2):
    return num1 - num2


# Multiplication
def multiply(num1, num2):
    return num1 * num2


# Division
def divide(num1, num2):
    return num1 / num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    num1 = int(input("Enter number: "))
    is_continue = True

    while is_continue:
        num2 = int(input("Enter number:"))

        for item in operations:
            print(item)
        symbol = input("Which operation you want to perform??")

        calculation_function = operations[symbol]

        answer = calculation_function(num1,num2)
        print(f"{num1}{symbol}{num2} is {answer}")

        repeat = input(f"Type 'y' to continue with current answer {answer} or type 'n' to start over again...").lower()
        if repeat == "y":
            num1 = answer
        else:
            is_continue = False
            calculator()

calculator()

