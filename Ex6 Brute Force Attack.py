# -*- coding: utf-8 -*-
"""
Exercise 6: Brute Force Attack
by Maria Angelica Gilleone Dy Rapsing

"""

correct_password="12345" # Define the correct password

max_attempts=5 # Input the maximum number of attempts
attempts=0

# Start a while loop for password entry
while attempts<max_attempts:
    user_input=input("Enter the password: ") # This is where the user will input the password

    # Check if the entered password is correct
    if user_input==correct_password:
        print("Access granted!")
        break
    else:
        attempts+=1
        remaining_attempts=max_attempts-attempts
        print(f"Incorrect password. You have {remaining_attempts} attempt(s) left.") # When the user types the incorrect password, it will deduct one attempt till it reaches 0

# Checks if the user has reached the maximum attempts
if attempts==max_attempts:
    print("Maximum attempts reached. Authorities have been alerted.")
