# heroku-library-catalogue
A library catalogue which uses Flask and runs on Heroku

### File structure of the app

    .
    ├── README.md    
    ├── requirements.txt
    ├── Procfile
    ├── run.py
    ├── app
         ├── index.py
         ├── templates
         └── static

## Heroku Commands to be used (assuming you have created the app already. Else see the url below)
URL: https://www.jcchouinard.com/deploy-a-flask-app-on-heroku/

Commands I use:
heroku login

git init
heroku git:remote -a lib-test-ak
git remote -v

git add .
git commit -m "Adding Spreadsheets"

git push heroku dev:master

heroku ps:scale web=1