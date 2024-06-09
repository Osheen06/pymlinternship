# Write a python program that calculates the sum of the digits of a given number

def sum_of_digits(number):
    number_str = str(number)
    total_sum = 0
    for digit in number_str:
        total_sum += int(digit)
    return total_sum

# Input from the user
number = int(input("Enter a number: "))

# Calculate the sum of digits
result = sum_of_digits(number)

# Print the result
print(f"The sum of the digits of the number {number} is: {result}")
