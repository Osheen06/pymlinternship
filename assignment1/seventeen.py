# Write a program in python that converts a given string to title case (first letter of each word capitalized).

def titlestring(str1):
    title_case_string = str1.title()
    return title_case_string

str1 = input("Enter a string: ")

# Convert the string to title case
title_case_result = titlestring(str1)

# Print the result
print("String in title case:", title_case_result)

    