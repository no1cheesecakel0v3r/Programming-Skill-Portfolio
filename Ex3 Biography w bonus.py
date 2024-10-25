"""
Exercise 3: Biography
by Maria Angelica Gilleone Dy Rapsing

"""
# Created a dictionary containing my biography information
biography={
    "Name":"Angelica Rapsing", 
    "Hometown":"Sharjah",
    "Age":"19"
           }

for x,y in biography.items():
    print(x,":",y) # This will print out the key and value in the dictionary that contains my information

# Created a dictionary that will contain the biography information by the user's input
biodict={
    "Name":input("Enter your first and last name: "),
    "Hometown":input("Enter your hometown: "),
    "Age":input("Enter your age: ")
         }

for x,y in biodict.items():
    print(x,":",y) # This will print out the title key and its value and show the user's biography they've inputted