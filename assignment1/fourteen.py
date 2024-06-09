# Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

def read_multiple_lines():
    print("Enter your lines of text. Press Enter on an empty line to finish.")
    
    # Initialize an empty list to store the lines
    lines = []
    
    while True:
        # Read a line of input from the user
        line = input()
        
        # If the line is empty, break the loop
        if line == "":
            break
        
        # Add the line to the list
        lines.append(line)
    
    # Print all the lines
    print("\nYou entered:")
    for line in lines:
        print(line)

# Call the function
read_multiple_lines()
