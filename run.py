# ********************** THIS REPRESENTS 80 CHARACTERS ********************** #

import sys
from time import sleep
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import matplotlib.pyplot as plt

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

CREDENTIALS = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
GSPREAD_CLIENT = gspread.authorize(CREDENTIALS)
SPREADSHEET = GSPREAD_CLIENT.open('Cantina Satisfaction Survey')


class Question:
    def __init__(self, number, name, options_num_values, options_text_values):
        self.number = number
        self.name = name
        self.options_num_values = options_num_values
        self.options_text_values = options_text_values


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
        show_results()
    elif user_input.lower() == "e":
        if confirm_exit():
            some_spacing = "\n" * 12
            good_bye_message = f"{some_spacing}    Thank you for your visit! Have a great day!{some_spacing}"
            sys.exit(good_bye_message)
        else:
            display_menu_options(user_answers, starting_question)
    else:
        print("    !! answer not valid !!")
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
    for i in range(starting_question, 21):
        choices = dict(zip(questions[i].options_num_values, questions[i].options_text_values))
        answer = display_question(questions[i], choices)
        if answer in "mesr":
            verify_menu_answers(user_answers, starting_question, answer)
        else:
            user_answers.append(choices[int(answer)])
            starting_question += 1
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
    print(f"    {question.number}. {question.name}")
    for i in range(1, len(choices) + 1):
        if choices[i] != "":
            print(f"        {i} - {choices[i]}")
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
    !! answer not valid !!
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
    !! answer not valid !!
    You must choose among the suggested answers!
            """)
            return False
        else:
            return True


def show_results():
    survey_text_results = get_results_from_worksheet()
    survey_num_results = convert_results_into_num(survey_text_results)
    average_satisfaction_per_question = []
    print()
    for question in questions:
        average_satisfaction_per_question.append((question.name, sum(column:=survey_num_results.get(question.name)) / len(column)))
    print(average_satisfaction_per_question)
    overall_satisfaction_average = calculate_overall_satisfaction_average(average_satisfaction_per_question)
    print(overall_satisfaction_average)
    convert_changing_request_into_chart(survey_text_results)


def calculate_overall_satisfaction_average(average_satisfaction_per_question):
    return sum(list_of_average:=[average[1] for average in average_satisfaction_per_question[2:-1]]) / len(list_of_average)


def convert_changing_request_into_chart(survey_text_results):
    change_request = survey_text_results.pivot_table(index= ["If you could change one thing about the cantina, what would it be?"], aggfunc= "size")
    change_request.plot(kind="bar")
    plt.show()


def get_results_from_worksheet():
    return pd.DataFrame(SPREADSHEET.worksheet("Survey results").get_all_records())


def convert_results_into_num(dataframe_results):
    new_dataframe = dataframe_results.copy()
    for question in questions:
        new_dataframe.replace(question.options_text_values, question.options_num_values, inplace=True)
    return new_dataframe


if __name__ == "__main__":
    questions_df = pd.DataFrame(SPREADSHEET.worksheet("Survey questions").get_all_records())
    questions = []
    for i in range(0, 101, 5):
        question_number = questions_df.at[i, "Question numbers"]
        question_name = questions_df.at[i, "Questions"]
        options_num_val = []
        options_text_val = []
        for j in range(5):
            if questions_df.at[i+j, "text values"] != "":
                options_num_val.append(questions_df.at[i+j, "numeric values"])
                options_text_val.append(questions_df.at[i+j, "text values"])
        questions.append(Question(question_number, question_name, options_num_val, options_text_val))
    user_answers = []
    starting_question = 0
    display_menu(user_answers, starting_question)
