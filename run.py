# ********************** THIS REPRESENTS 80 CHARACTERS ********************** #

import sys
from time import sleep
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
GSPREAD_CLIENT = gspread.authorize(CREDENTIALS)
SPREADSHEET = GSPREAD_CLIENT.open('Cantina Satisfaction Survey')


def display_menu(user_answers, starting_question):
    """
    This function display the welcoming message of the application
    as well as the main commands to navigate within the application
    """
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

    display_menu_options(user_answers, starting_question)
    

def display_menu_options(user_answers, starting_question):
    """
    This function display the commands available to navigate within the
    application
    """
    print("""
    The basic commands of our survey are as below and can be used at anytime:
        - (m) or (M) --> menu
        - (s) or (S) --> survey
        - (r) or (R) --> results
        - (e) or (E) --> exit
    """)
    user_choice = input("    What do you want to do?\n")
    verify_menu_answers(user_answers, starting_question, user_choice)


def verify_menu_answers(user_answers, starting_question, user_input):
    """
    This function takes a user input as a parameter and decides what to 
    run next
    """
    if user_input.lower() == "m":
        display_menu(user_answers, starting_question)
    elif user_input.lower() == "s":
        display_survey(user_answers, starting_question)
    elif user_input.lower() == "r":
        pass  # ----------------------------------------------- TO BE IMPLEMENTED !
    elif user_input.lower() == "e":
        if confirm_exit():
            some_spacing = "\n" * 12
            good_bye_message = f"{some_spacing}    Thank you for your visit! Have a great day!{some_spacing}"
            sys.exit(good_bye_message)
        else:
            display_menu_options(user_answers, starting_question)
    else:
        print("    Your answer is not valid.")
        display_menu_options(user_answers, starting_question)


def confirm_exit():
    """
    This function verify if the user confirm the exit command and 
    return a boolean
    """
    confirm = input("""
    If you started the survey, you will lose your progress.
    Do you really want to exit the application ([y]/n)?\n
    """)
    if confirm == "y":
        return True
    False


def display_survey(user_answers, starting_question):
    """
    This function display all the questions, one after another and collects the answers 
    from the user
    """
    print("    **************************** S U R V E Y ****************************")
    for i in range(starting_question, 122, 6):
        possible_answer_num = [
            int(element[0]) for element in SPREADSHEET.worksheet("Survey questions").get(f"B{i+1}:B{i+5}")
        ]
        possible_answer_text = [
            element[0] for element in SPREADSHEET.worksheet("Survey questions").get_values(f"C{i+1}:C{i+5}")
        ]
        choices = dict(zip(possible_answer_num, possible_answer_text))
        question = SPREADSHEET.worksheet("Survey questions").get_values(f"B{i}")[0][0]
        answer = display_question(question, choices)
        if answer in "mesr":
            verify_menu_answers(user_answers, starting_question, answer)
        else:
            user_answers.append(choices[int(answer)])
            starting_question += 6
        sleep(5)
    current_survey_results = SPREADSHEET.worksheet('Survey results')
    current_survey_results.append_row(user_answers)
    print()
    print("""
    We are done here.
    Your answers have been submitted successfully.
    Thank you for filling in our survey!
    """)

    display_menu_options(user_answers, starting_question)


def display_question(question, choices):
    """
    This function is recursive. it displays a question of the survey and 
    verify if the answer of the user is valid. If it is not, it calls 
    itself again until the input is as expected
    """
    print()
    print(f'    {question}')
    for num, text in choices.items():
        print(f"        {num} - {text}")
    print()
    answer = input("Your answer: \n")
    if answer_is_valid(answer, choices):
        return answer
    else:
        return display_question(question, choices)


def answer_is_valid(user_input, choices):
    """
    This function verify if an input is valid.
    It takes as parameters:
     - the user input
     - the possible answers for the related question
    """
    try:
        int(user_input)
    except ValueError:
        if user_input.lower() not in "mesr" or user_input.lower() == "":
            print("""
    Your answer is not valid.
    Remember, the main commands are: 
        - (m) or (M) for the menu
        - (s) or (S) for the survey
        - (r) or (R) for the results
        - (e) or (E) to exit the application
            """)
            return False
        else:
            return True
    else:
        if int(user_input) not in range(1, len(choices) + 1):
            print(f"""
    Your answer is not valid.
    You must choose among the suggested answers!
            """)
            return False
        else:
            return True


if __name__ == "__main__":
    user_answers = []
    starting_question = 1
    display_menu(user_answers, starting_question)
