# Write a program that asks the user for their birth year and calculates their age.

from datetime import datetime
def calculate_age(birth_year):
    # Get the current year
    current_year = datetime.now().year
    
    # Calculate the age
    age = current_year - birth_year
    
    return age

# Input from the user
birth_year = int(input("Enter your birth year: "))

# Calculate the age
age = calculate_age(birth_year)

# Print the result
print(f"You are {age} years old.")
