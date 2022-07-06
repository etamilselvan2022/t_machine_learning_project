## Start Machine Learning project.

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
```

To activate environment
```
conda activate venv
```
or
```
conda activate venv/
```

To install all requirements mentioned in requirements.txt file
```
pip install -r requirements.txt
```

To add files to git
```
git add .
```
or
```
git add <file name>
```
or
```
git add <filename1> <filename2>
```

> Note: to ignore file or folder from git we can write name of file/folder in .gitignore file

to create version/commit all changes by git
```
git commit -m "message"
```

to send version/changes to github
```
git push origin main
```

to check git status
```
git status
```

to check versions maintained by git
```
git log
```

to check remote url
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = etamilselvan2022@gmail.com
2. HEROKU_API_KEY = 8eb724b7-4d2c-4c6e-bbc5-905df68066f4
3. HEROKU_APP_NAME = mlapp-16072022