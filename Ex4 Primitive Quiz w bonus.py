"""
Exercise 4: Primitive Quiz
by Maria Angelica Gilleone Dy Rapsing

"""

questions = {  # A list of 10 European countries and their capitals for the quiz
        "France": "Paris",
        "Germany": "Berlin",
        "Italy": "Rome",
        "Spain": "Madrid",
        "Portugal": "Lisbon",
        "Netherlands": "Amsterdam",
        "Belgium": "Brussels",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Finland": "Helsinki"
    }

for country, capital in questions.items(): # Go through the questions over and over again but with each country and capital
    answer = input(f"What is the capital of {country}? ").strip() 
    if answer.lower() == capital.lower():    # This is to check the answer ignoring the different capitalization of the letters
            print("Correct! Well done.\n")
    else:   
        print(f"Wrong! The correct answer is {capital}.\n")

