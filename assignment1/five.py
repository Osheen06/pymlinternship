# Write a program that takes a string input from the user and writes it to a text file.

def write_to_file():
    # Get input from the user
    user_input = input("Enter the string you want to write to the file: ")

    # Specify the filename
    filename = "output.txt"

    try:
        # Open the file in write mode
        with open(filename, 'w') as file:
            # Write the user input to the file
            file.write(user_input)
        
        print(f"The string has been written to {filename}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
write_to_file()
