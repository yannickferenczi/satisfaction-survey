# Cantina Satisfaction Survey

[The live project is visible here](https://cantina-satisfaction-survey.herokuapp.com/)

---
## Table of Contents

1. [User Experience](#user-experience)
2. [Technologies Used](#technologies-used)
3. [Testing](#testing)
4. [Bugs](#bugs)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

---
## User Experience (#user-experience)

---
## Technologies Used (#technologies-used)

---
## Testing (#testing)

---
## Bugs (#bugs)

---
## Deployment (#deployment)

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

---
## Credits (#credits)

---
## Acknowledgements (#acknowledgements)
