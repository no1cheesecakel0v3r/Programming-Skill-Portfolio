"""
Exercise 10: Is it even?
by Maria Angelica Gilleone Dy Rapsing

"""

# Create a function to determine if the number is odd or even
def check_even_odd(number): 
    """Determine if the number is even or odd."""
    if number%2==0:
        return f"{number} is even." # If the number is even number, it will print this
    else:
        return f"{number} is odd." # If the number is an odd number, it will print this

def main():
    # Ask the user for a number
    user_input=input("Enter a number: ")
    
    # Convert the input to an integer
    try:
        number=int(user_input)
        
        # Call the function and print the result
        result=check_even_odd(number)
        print(result) 
    except ValueError: # Will check if the user has given a valid number
        print("Please enter a valid integer.") # If not given a valid number, this will print out

if __name__=="__main__":
    main()