# Write a program that copies the contents of one text file to another.

def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            content = source.read()
    
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Contents of '{source_file}' have been copied to '{destination_file}'.")
    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input filenames from the user
source_file = input("Enter the filename of the source text file: ")
destination_file = input("Enter the filename of the destination text file: ")

# Copy the contents of the source file to the destination file
copy_file(source_file, destination_file)
