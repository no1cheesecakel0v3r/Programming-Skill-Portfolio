"""
Exercise 8: Simple Search
by Maria Angelica Gilleone Dy Rapsing

"""

# Initialize the list of names
names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

# Allow the user to input the search term
search_term=input("Enter the name you want to search for: ")

# Search for the name in the list
if search_term in names:
    print(f"{search_term} was found in the list.")
else:
    print(f"{search_term} was not found in the list.")
