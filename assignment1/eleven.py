# Write a python program that generates the first n numbers in the Fibonacci sequence.

def generate_fibonacci(n):
    # Initialize the first two Fibonacci numbers
    fib_sequence = [0, 1]
    
    # Generate the Fibonacci sequence up to n numbers
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    
    return fib_sequence[:n]

# Input from the user
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Ensure n is a positive integer
if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_numbers = generate_fibonacci(n)
    print(f"The first {n} numbers in the Fibonacci sequence are: {fibonacci_numbers}")
