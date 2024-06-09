# Write a python program that checks whether a given number is even or odd.
a = int(input("Enter a number : "))
def evenodd():
    if a%2==0:
        print("Number is even")
    elif a%2!=0:
        print("Number id odd")
    else : 
        print("Invalid character")
        
evenodd()