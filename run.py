# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

# -------------------- THIS REPRESENTS 80 CHARACTERS ------------------------ #

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
GSPREAD_CLIENT = gspread.authorize(CREDENTIALS)
SPREADSHEET = GSPREAD_CLIENT.open('Cantina Satisfaction Survey')


if __name__ == "__main__":
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