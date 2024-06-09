# Write a program that reads the content of a text file and prints it to the console.

def read_from_file():
    # Specify the filename
    filename = "output.txt"

    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            # Read the content of the file
            content = file.read()
        
        # Print the content to the console
        print("Content of the file:")
        print(content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
read_from_file()
