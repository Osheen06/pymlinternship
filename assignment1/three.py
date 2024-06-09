# Write a python program that calculates the factorial of a given number.
def fac(n):
    if n < 0:
        return "Invalid input: Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Input from the user
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {fac(number)}")
    