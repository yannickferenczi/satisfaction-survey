<div align="center">

# Cantina Satisfaction Survey


![deployment](https://img.shields.io/static/v1?label=deployed&message=Yes&color=success&style=plastic)
![deployment](https://img.shields.io/static/v1?label=plateform&message=Heroku&color=634987&style=plastic)

This is a command line application for a company cantina to reach out their customer with a survey and get some feedback to help them improve the quality of their service and better provide for the needs of the company employees.

[The live project is visible here](https://cantina-satisfaction-survey.herokuapp.com/)

</div>

---
---
## Table of Contents
[Cantina Satisfaction Survey](#cantina-satisfaction-survey)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Target Audience](#target-audience)
    - [User Stories](#user-stories)
  - [Design](#design)
    - [Flowchart](#flowchart)
    - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Testing](#testing)
    - [Syntaxe testing](#syntaxe-testing)
    - [Manual testing](#manual-testing)
    - [Features testing along with the User stories](#features-testing-along-with-the-user-stories)
  - [Bugs](#bugs)
    - [The fixed ones](#the-fixed-ones)
    - [The remaining ones](#the-remaining-ones)
  - [Deployment \& local development](#deployment--local-development)
    - [Deployment](#deployment)
    - [Local development](#local-development)
  - [Credits](#credits)
    - [Content](#content)
    - [Guidance](#guidance)
  - [Acknowledgements](#acknowledgements)



---
## User Experience (UX)

### Target Audience

The target audience of this application are the employees of the company offering a cantina service.

### User Stories

**As a first visitor:**

- As a first visitor, I want to understand the purpose of the application so that I can decide what to do. (US01)
- As a first visitor, I want to understand how to use the application so that I can use it easily. (US02)
- As a first visitor, I don't want to start the survey again from scratch if I unintentionally navigate out of it so that I don't waste my time answering again the same questions. (US03)

**As a returning visitor:**

- As a returning visitor, I want to easily navigate through the application so that I can quickly consult the results of the survey. (US04)
- As a returning visitor, I want to easily visualize the results of the survey so that I can get the outcome faster.
- As a returning visitor, I want a confirmation of my actions, so that I know things go right. (US06)

**As the service provider:**

- As the service provider, I want to get as many persons as possible to answer the survey so that I have a more relevant understanding of what are the needs of most of my customers. (US07)
- As the service provider, I want to get feedbacks from my customers so that I can improve my service. (US08)

---
## Design

The application has been design so that users can navigate through it, using some basic commands described within the application and exit the application whenever they decide.

### Flowchart

A flowchart has been made to demonstrate the expected behaviour of the application and help its development:

![here](documentation/logic-chart.png)

### Features

- F01: The application opens on a landing page displaying a welcoming message and describing its main commands: 

    ![here](documentation/landing-page.png)

- F02: The application display a survey and get the answers from the users:

    ![here](documentation/survey.png)

- F03: The application verify the answers of the user and display a warning if they are not valid:

    ![here](documentation/answer-invalid.png)

- F04: The application display a message to thank the users when their survey has been fully submitted: 

    ![here](documentation/answers-submitted.png)

- F05: Users are asked to confirm when they want to exit the application:

    ![here](documentation/confirmation-message.png)

- F06: Users receive a nice greeting when exiting the application:

    ![here](documentation/good-bye-message.png)

- F07: The application displays the results of the survey:

    ![here](documentation/results.png)

- F08 The application collects the results into graphs for a better visualisation:

    ![here](documentation/results-details.png)

---
## Technologies Used

Language

- Python

Frameworks and other Programs

- The python module Pandas has been used to organise and manipulate the data
- The python module plotext has been used to display graphs within the command line
- Google has been used to storaged data and access them via an API
- Google sheets has been used as a data base.
- gspread api has been used to link the script to the data base.
- [Mockaroo](https://www.mockaroo.com/) has been used to generate data to fullfil the survey with fake random customers.
- [tinypng](https://tinypng.com/) has been used to reduce the size of the screenshots display in the README.md file.
- [Shields.io](https://shields.io/) has been used to add badges to the README

---
## Testing

### Syntaxe testing

The code of run.py has been checked using the [CI Python Linter](https://pep8ci.herokuapp.com/).

It has been complicated to solve the "line too long issues". But after some research and some tips from other developers within the python community, I managed to get rid of all of them: 

![pyhton checker results](documentation/python-checker.png)

### Manual testing

![passed](https://img.shields.io/static/v1?label=passed_test&message=11&color=success&style=plastic)

| Tests | Results |
| :--- | :---: |
| When opening the application, the welcoming message and the main commands are displayed | pass |
| When typing (s) or (S) at the first time, the first question is displayed | pass |
| When answering any question with one of the number matching a proposition, the next question is displayed | pass |
| At any time, when typing something else than one of the expected character, a message 'answer invalid' is displayed and users are asked again what they want to do | pass |
| When typing one of the main command anywhere within the application, the main command is executed | pass |
| At any time, When typing the command to exit the application, users are asked for confirmation with a warning that the progress in the survey will be lost if not fully complete | pass |
| When users navigate to other area from a started survey and go back to the survey area, the last not answered question is displayed | pass |
| Within the same 'connection', meaning as long as the page is not being reloaded, users can not refill the survey | pass |
| When a survey has been fully completed, the answered are saved into the google worksheet | pass |
| When typing (r) or (R), users are led to the results area and the overall satisfaction average is displayed | pass |
| From the results area, while typing (d) or (D), a graph per question representing the results are displayed | pass |


### Features testing along with the User stories

| Features \ User Stories | US01 | US02 | US03 | US04 | US05 | US06 | US07 | US08 |
| --- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| F01 | X | X |   |   |   |   | X |   |
| F02 |   |   |   |   |   |   |   | X |
| F03 |   |   |   |   |   | X | X |   |
| F04 |   |   |   |   |   | X |   |   |
| F05 |   |   | X |   |   | X |   |   |
| F06 |   |   |   |   |   | X |   |   |
| F07 |   |   |   | X | X |   |   |   |
| F08 |   |   |   |   | X |   |   |   |

---
## Bugs

### The fixed ones

- The dataframe created out of the results google worksheet is fullfilled with text for the users to easily understand how to answer. Nevertheless, for some average calculation, I needed to convert those text into their corresponding numerical values. The tricky part is that I had to replace one column after another as some textual values were common to different column but their corresponding numerical values were not identical. So I first used the replace method on the dataframe, with the inplace parameter set to false and assigning the new dataframe to a new variable and using a for loop iterating over every column (or otherwise said: every question). But then only the column from the last iteration would actually have the values replaced.
So I tried to switch the inplace parameter to False. But then later on when I needed to access the dataframe with the textual values in it, it was gone. So I solved this by creating a copy of the dataframe.
- At first, I was requesting data with the google sheets API for every single question. Unfortunately, too many requests of the google sheets API in a short time raises an error. To solve this problem, I implemented one request for the full list of questions. Nevertheless, to do so I had to reorganize the data in the worksheet.
- The way I implemented some if statement, typing the 'enter' key on the keyboard was considered a valid answer. To fix this issue, I had to write an if statement in the case of an empty string.
- To display the results as a graph, I first wanted to use the matplotlib library. For some reasons, the code would not raise any error nor break down, but the graph would not show up. I am not sure about this, but I might have understood that those graphs would not show up in a command line. I found another library (plotext) which display graphs within the command line. That solved my problem.

### The remaining ones

- When typing the exit command (e) or (E) while progressing through the survey, users are asked to confirm. If they cancel, with answering no to the confirmation, users are led back to the main menu. It is not a big issue as they can go back at the question they had not answered yet by typing the survey command (s) or (S). But it is a weird behaviour and gives a poor user experience. This could be solved with more time by adding a specific verification when the exit command is used within the survey.

---
## Deployment & local development

### Deployment

The application has been deployed on Heroku with the following steps:

1. I first made sure that the requirements.txt file was up to date with the used dependencies of the project by opening a terminal from the main directory and typing the following command:<br>
    pip freeze > requirements.txt
2. Then I staged, commited and pushed all changements using the git command in the terminal:<br>
    git add .<br>
    git commit -m "Add requirements for deployment"<br>
    git push
3. Then I went to [Heroku](https://dashboard.heroku.com/apps) and logged into my free account.
4. From my Heroku dashboard, I clicked on the button "New", in the top right corner of the dashboard and then clicked on "Create new app".
5. In the "Create New App" form which just opened, I gave a name to my application and selected Europe as a region. The app name must be unique. Therefore, I had call mine cantina-satisfaction-survey as satisfaction-survey was already used and not available anymore.
6. I confirm the creation of the app by clicking the "Create app" button, just underneath the form.
7. Within the created app, I opened the Settings tab.
8. From the Settings tab, I scrolled down to the Config Vars. I needed to add two condig variables:
    - The first one was to add the needed confidential information for my script to access my google spreadsheet. 
    - The second one to add the port.
9. So I clicked the "Reveal Config Vars" button.
10. In the first "KEY" field, I typed CREDS (in uppercase) and in the "VALUE" field, I paste the content of my creds.json file (which is a key created with the google drive API, to allow my script to access to my google spreadsheet) and clicked the add button.
11. In the second "KEY" field, I typed PORT (also in uppercase) and 8000 in the corresponding "VALUE" field and again clicked the add button.
12. I then went further down to the Buildpacks to add the needed dependencies.
13. I clicked the "Add buildpack" button, selected python and confirm with the "Save changes" button.
14. I repeated the steps, selecting nodejs.
15. I finally reached the Deploy tab (from the very top of the page).
16. In the deployment method, I have selected GitHub.
17. Then I searched the name of the repository I wanted to deploy (satisfaction-survey).
18. I then clicked the "Connect" button next to the name of my project repository.
19. Then I clicked the "Enable Automatic Deploys" button further down.
20. And finally clicked the "Deploy Branch" button underneath.

[The live project is visible here](https://cantina-satisfaction-survey.herokuapp.com/)

### Local development

To use this project on your own, you will need to create a spreadsheet with a certain format. The 'sample_spreadsheet.xlsx' in the assets directory of this project should be used as a template to recreate the one currently linked to the live project.
Then in the line 17 of run.py, the string should match the name of the spreadsheet.
And the creds.json file should contain your own credentials. You can create it using the google drive api. More information on [how to get your gspread credentials](https://docs.gspread.org/en/v5.7.1/oauth2.html#enable-api-access). 

**How to fork**

1. Log in to [GitHub](https://github.com/).
2. [Click here](https://github.com/yannickferenczi/satisfaction-survey) to go to the repository of this project
3. Click the Fork button in the top right corner.

**How to clone**

1. Log in to [GitHub](https://github.com/).
2. [Click here](https://github.com/yannickferenczi/satisfaction-survey) to go to the repository of this project
3. Click on the code button, select whether you would like to clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open the terminal in your code editor and change the current working directory to the location you want to use for the cloned directory.
5. Type 'git clone' into the terminal and then paste the link you copied in step 3. Press enter.

---
## Credits

### Content

The content has been entirely created by the programmer of this app.

### Guidance

- [Real Python](https://realpython.com/documenting-python-code/) has been used to document the code


---
## Acknowledgements

Thank you to Alan, my facilitator at [Code Institute](https://codeinstitute.net/de/), for supporting me on this project, as I could not manage to organize an appointment with my mentor.

Thank you to my friends and family who helped me test the survey.