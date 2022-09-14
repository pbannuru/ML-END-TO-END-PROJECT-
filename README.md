# ML-END-TO-END-PROJECT-
This is a machine learning project where all end to end deployement code is available.

# Software and account Requirement: - 

1. Github Account

2. Heroku Account

3. VS Code IDE

4. GIT cli

5. GIT Documentation

# Creating conda environment

conda create -p venv python==3.7 -y

conda activate venv/
OR

conda activate venv

# pip install -r requirements.txt

# To Add files to git

1. git add .
OR

2. git add <file_name>
## Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

# To check the git status

1. git status

# To check all version maintained by git

1. git log

# To create version/commit all changes by git

1. git commit -m "updated"
# To send version/changes to github

1. git push origin main
# To check remote url

1. git remote -v
# To setup CI/CD pipeline in heroku we need 3 information

1.HEROKU_EMAIL = pbannuru@gmail.com

2. HEROKU_API_KEY = f2ccae77-156e-4e59-be69-59531739708c

3. HEROKU_APP_NAME = mlcicdapp

# BUILD DOCKER IMAGE

1. docker build -t ml-project:end-to-end .

Note: Image name for docker must be lowercase

# To list docker image

1. docker images
# Run docker image

1. docker run -p 5000:5000 -e PORT=5000 d9df7a76c930
# To check running container in docker

1. docker ps

# Tos stop docker conatiner

1. docker stop <container_id>
# python setup.py install
1. Install ipykernel

2. pip install ipykernel

# Data Drift: When your datset stats gets change we call it as data drift

<<<<<<< HEAD
>>>>>>> 3458294a99f32ffa3e48a65a350bcac317571ce9

deployed app:

https://mlcicdapp.herokuapp.com/
