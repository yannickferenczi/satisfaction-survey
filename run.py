# -------------------- THIS REPRESENTS 80 CHARACTERS ------------------------ #

import sys
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
GSPREAD_CLIENT = gspread.authorize(CREDENTIALS)
SPREADSHEET = GSPREAD_CLIENT.open('Cantina Satisfaction Survey')

def display_menu():
    print("""
    Welcome to the Employee Cantina Satisfaction Survey!

    At our company, we believe that a satisfied and nourished workforce is 
    essential for productivity and well-being. We value the opinions and 
    experiences of our employees, and your feedback will help us enhance our 
    employee cantina services to better meet your needs.

    This survey of 20 questions aims to gather your thoughts and suggestions 
    regarding various aspects of our employee cantina, including the quality 
    of food, variety of menu options, cleanliness, staff friendliness, and 
    overall dining experience. We are committed to providing a positive and 
    enjoyable dining environment that caters to your preferences and dietary 
    requirements.

    Your input is invaluable to us. By participating in this survey, you have 
    the opportunity to voice your opinions, highlight areas of improvement, 
    and contribute to the continuous enhancement of our cantina services. 
    Rest assured that your responses will be treated with strict 
    confidentiality, and the data collected will be used solely for the 
    purpose of improving our employee cantina.

    IMPORTANT NOTE: for your identity to remain secret, we have decided not 
    to ask any information to help us track who filled in this survey. We 
    believe that doing so we provide us trulier information. In return, for 
    the results to be representative, we kindly ask you to fill in the form 
    only once.
    """)

    # Main area of the application:
    print("- Type (m) or (M) to go to the menu\n")
    print("- Type (e) or (E) to exit the application\n")
    print("- Type (s) or (S) to start the survey\n")
    print("- type (r) or (R) to see the current results of the survey\n")

    user_choice = input("What do you want to do?\n")
    if user_choice.lower() == "m":
        display_menu()
    elif user_choice.lower() == "e":
        sys.exit("Thank you for your visit! Have a great day!")
    elif user_choice.lower() == "s":
        display_survey()


if __name__ == "__main__":

    display_menu()

    for i in range(1, 8, 6):
        possible_answer_num = [int(element[0]) for element in SPREADSHEET.worksheet("Survey questions").get(f"B{i+1}:B{i+5}")]
        possible_answer_text = [element[0] for element in SPREADSHEET.worksheet("Survey questions").get_values(f"C{i+1}:C{i+5}")]
        choices = dict(zip(possible_answer_num, possible_answer_text))
        print(choices)
        print()
        print(SPREADSHEET.worksheet("Survey questions").get_values(f"B{i}")[0][0])
        for num, text in choices.items():
            print(num, text)
        print()
