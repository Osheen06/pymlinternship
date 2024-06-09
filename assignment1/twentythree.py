# Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Input from the user
choice = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ")

if choice.upper() == 'C':
    celsius = float(input("Enter temperature in Celsius: "))
    converted_temp = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {converted_temp}°F.")
elif choice.upper() == 'F':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    converted_temp = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {converted_temp}°C.")
else:
    print("Invalid choice! Please enter 'C' or 'F'.")

