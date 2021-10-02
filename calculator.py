# Function with output
from art import logo_1, logo_2

# def format_name(f_name, l_name):
#     """Take a first and last name and format it
#     to return the title case version of the name.""" # docstring, use to describe a func
#     if f_name == "" or l_name == "":
#         return
#     formatted_f_name = f_name.title()
#     formatted_l_name = l_name.title()

#     return f"{formatted_f_name} {formatted_l_name}"

# name = format_name("ray", "akime")

# print(name)

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 # print("Leap year.")
#                 return True
#             else:
#                 # print("Not leap year.")
#                 return False
#         else:
#             # print("Leap year.")
#             return True
#     else:
#         # print("Not leap year.")
#         return False

# def days_in_month(year, month):
#     if month > 12 or month < 1:
#         return "Invalid month"
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap(year) and month == 2:
#         return 29
#     return month_days[month - 1]


# # Do NOT change any of the code below

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# Calculator program

# Add
def add(n1, n2):
    return n1 + n2

# Substract
def substract(n1, n2):
    return n1 - n2

# Multiply
def multiply(n1, n2):
    return n1 * n2

# Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,    
}


cal_art = '''

'''

def calculator():
    print(logo_1)
    print(logo_2)
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:

        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_func = operations[operation_symbol]
        
        answer = calculation_func(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exist.: ") == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()

