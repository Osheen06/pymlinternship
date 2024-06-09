# Write a program in python that converts a string into a list of its characters.

def string_to_list(input_string):
    char_list = list(input_string)
    return char_list

input_string = input("Enter a string: ")
char_list = string_to_list(input_string)


print("List of characters:", char_list)
