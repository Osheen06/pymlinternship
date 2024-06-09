# Write a python program that counts the occurrences of a specific element in a list.

def count_occurrences(lst, element):
    occurrences = lst.count(element)
    return occurrences

input_list = input("Enter a list of elements separated by spaces: ").split()

element_to_count = input("Enter the element to count occurrences: ")

lst = [int(item) if item.isdigit() else item for item in input_list]

occurrences = count_occurrences(lst, element_to_count)

print(f"The element '{element_to_count}' occurs {occurrences} times in the list.")
