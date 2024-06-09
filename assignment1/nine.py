# Write a python program that checks if a substring is present in a given string.

def check_substring():
    # Input the main string from the user
    main_string = input("Enter the main string: ")
    
    # Input the substring from the user
    substring = input("Enter the substring to check: ")
    
    # Check if the substring is in the main string
    if substring in main_string:
        print(f"The substring '{substring}' is present in the main string.")
    else:
        print(f"The substring '{substring}' is not present in the main string.")

# Call the function
check_substring()
