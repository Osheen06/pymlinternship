# Write a program in python that counts the frequency of each character in a string.

def count_character_frequency(input_string):
    # Initialize an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate over each character in the input string
    for char in input_string:
        # Increment the count of the character in the dictionary
        char_frequency[char] = char_frequency.get(char, 0) + 1

    return char_frequency

# Input string from the user
input_string = input("Enter a string: ")

# Calculate character frequencies
frequency = count_character_frequency(input_string)

# Print the result
print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")
