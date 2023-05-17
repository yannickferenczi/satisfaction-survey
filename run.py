# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
GSPREAD_CLIENT = gspread.authorize(CREDENTIALS)
SPREADSHEET = GSPREAD_CLIENT.open('Cantina Satisfaction Survey')
