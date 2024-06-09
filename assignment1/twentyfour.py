# Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result

def calculate(num1, num2, operator):
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero is not allowed."
    else:
        result = "Error! Invalid operator."
    return result

# Input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")

# Calculate the result
result = calculate(num1, num2, operator)

# Print the result
print(f"The result of {num1} {operator} {num2} is: {result}")
