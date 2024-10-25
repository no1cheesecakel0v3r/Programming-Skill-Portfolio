"""
Exercise 5: Days of the Month
by Maria Angelica Gilleone Dy Rapsing

"""

days_in_month={ # Creating a dictionary containing the months and days of a year, including leap year
        1: 31,  # January
        2: 28,  # February (default, will adjust for leap years)
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September   
        10: 31, # October
        11: 30, # November
        12: 31  # December
    }

month = int(input("Enter the month number (1-12): ")) # Asks user for month number

if 1<=month<=12: # Check if the month number is valid
    if month==2:  # Special case for February
        year = int(input("Enter the year: "))  # Check for leap year
        if (year%4==0 and year%100!=0) or (year%400==0):
            days=29 # Leap year
        else:
             days=days_in_month[month]   # Regular year
    else:
        days=days_in_month[month]

    print(f"The number of days in month {month} is: {days}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")

