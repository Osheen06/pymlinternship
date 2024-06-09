# Write a python program that takes a list of numbers and returns their sum.

def calculate_sum(numbers):
    total_sum = sum(numbers)
    
    return total_sum
input_numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in input_numbers]
result = calculate_sum(numbers)

print("The sum of the numbers is:", result)
