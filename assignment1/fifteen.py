# Write a program that reads data from a CSV file and prints it to the console.

import csv

def read_csv_file(filename):
    try:
        # Open the CSV file for reading
        with open(filename, mode='r') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)
            
            # Read and print each row in the CSV file
            for row in csv_reader:
                print(row)
                
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input from the user
filename = input("Enter the filename of the CSV file: ")

# Call the function to read and print the CSV file
read_csv_file(filename)
