# Write a python program that returns the minimum and maximum values in a list of numbers

def find_min_max(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    
    return min_value, max_value

# Input list of numbers from the user
input_numbers = input("Enter a list of numbers separated by spaces: ").split()

# Convert input strings to integers
numbers = [int(num) for num in input_numbers]

# Find the minimum and maximum values
min_value, max_value = find_min_max(numbers)

# Print the result
print(f"The minimum value in the list is: {min_value}")
print(f"The maximum value in the list is: {max_value}")
