# NATURAL HEALING WIKI
![Screenshot Responsiveness](/static/images_readme/screenshot_responsiveness.PNG)

Natural Healing Wiki is a web application that is operated similarly to a normal wiki. 

The purpose of the application is to share knowledge about natural healing in the form of informative articles and allow users to create new contributions.

Users can view articles written by other users or administrators and create their own articles. However, only own articles can be edited. Before publication, articles created by users must be checked by administrators for appropriate content and then authenticated.

Click [here](https://natural-healing-wiki.herokuapp.com/) to live site.

## User Stories
---

GitHub issues were used to document user stories. 
The following categories were assigned for prioritization purposes: "Must Have", "Should Have", "Could Have" and "Won't Have".

### Fulfilled User Stories
- As a Site Admin, I can create, read, update and delete articles, so that I can manage my wiki content.
- As a Site User, I can view a list of all articles, so that I can select one to open & read.
- As a Site User, I can click on an article, so that I can read the full article.
- As a Site User, I can register an account, so that I can write articles and comments.
- As a Site User, I can write an article about natural healing, so that I can enlarge the wiki.
- As a Site User, I can edit articles, so that I can edit articles I have written myself after they have been created.
- As a Site User, I can delete articles, so that I can delete self-authored articles after creating them.
- As a Site Admin, I can approve or disapprove articles written by users, so that I can filter out faulty or unsuitable articles.

### User Stories for next release
- As a Site User, I can leave comments on an article, so that I can share my opinion about this article with others.
- As a Site User, I can view the comments of a specific article, so that I can read the added comments.
- As a Side Admin, I can approve or disapprove comments written by users, so that I can filter out faulty or unsuitable comments.
- As a Site User, I can view different categories and choose from them, so that I can view the associated articles.
- As a Site User, I can choose a category for my written article, so that my article gets assigned a category.
- As a Site User / Admin, I can create draft articles, so that I can finish writing the content later.

## Agile Methodology
---
![Screenshot User Stories](/static/images_readme/screenshot_userstories.PNG)

MoSCoW priority setting was used to create an agile project via GitHub Issues. 

Link to the project with live issues can be found [here](https://github.com/users/LucaNoah/projects/8).


## Wireframes
---
The web application was designed on a laptop screen size. This wireframe was used:

![Image Wireframe](/static/images_readme/wireframe-nhw.PNG)

The design has evolved during the development of the project in such a way that the sidebar was omitted and the entire functionality of these two elements gives way to the navbar.

## Existing Features
---
### - Navbar
On the left side, the logo is displayed with a link to the home page. Next to it, you can navigate to all articles or the articles created by the logged-in user via a drop-down menu. Further to the right is the navigation element for creating a new article. This element is only linked if the user is logged in. If the user is not logged in, its status is represented by a visual missing function. Even further to the right are the options to register or log in. If you are already logged in, logout is displayed there. On the far right are 2 social media icons that are connected to a link to the respective website that opens in a new window.

### - Register
Via the navbar the user has the possibility to get to a page to register. 
For this purpose, only username and password are required.

### - Log In
If the user has already registered, he can navigate via the navbar to the login page to log in with username and password.

### - Log Out
If the user is logged in, he can navigate to the logout page via the navbar.

### - Home Page
The home page of the application informs the user about the benefits and the target audience of the website. 
In addition, procedures are explained in more detail.

### - All Articles
All authored and authenticated articles are displayed here and listed by authoring date. 
Clicking on "Read" opens the respective article.

### - User Articles
In the same dropdown menu as all articles, there is a navigation named "Your Articles" which leads to a page that displays all articles of the currently logged-in user in chronological order.

### - Article Detail
By pressing the "Read" button below an article, the user is redirected to the corresponding article. The title, the name of the author, the date of creation, the description and the content are displayed. If the logged-in user is the author, the buttons "Edit" and "Delete" are visible at the very end.

### - Create Article
On this page, logged-in users can write articles. To do this, you are required to enter a title, description and related content. The Author field is automatically filled in based on the username. The author will be informed that his article will be styled and authenticated before publishing. He will also be asked to provide references if necessary. If Create is pressed, the user is asked again via modal whether his interaction should be carried out.

### - Edit Article
At the bottom of the article detail page, if the logged-in user is also the author, the "Edit" button is displayed. This will take the user to a page to edit the associated article. The page is built the same as the page to create an article, with the difference that the fields with the related information are prefilled.

### - Form Validation
When the user fills in the form to create or edit, it is validated by HTML attributes. 
The user cannot submit empty fields and is limited in the length of the characters.

### - Delete Article
At the bottom of the article detail page, if the logged-in user is also the author, the "Delete" button is displayed. With this button, the user can delete the article from the database after validating the request via modal.

### - Approve article
As an admin, articles written by users can be authenticated via the admin panel. 
Only then will they be displayed on the website.

### - Manage Articles & Users
As an administrator, articles and users can be managed via the admin panel.

## Future Features
---
### - Comments
It is planned that under the detail view and under the heads for editing and deleting comments from users can be displayed and added via an edit field.

### - Approve Comments
As an admin, comments written by users can be authenticated via the admin panel. 
Only then will they be displayed on the website.

### - Categories
In the same dropdown menu as All Articles and Your Articles, a link to categories should be added where the user can view the corresponding items from different categories.
These categories should also be available when creating and editing.

## Technologies Used
---
### Languages Used
- HTML5
- CSS3
- Python
- Django
- jQuery
- JavaScript

### Technologies and Programs Used
- GitHub was used for version control and planning/user stories of the agile project. 
- GitPod was used as IDE to write the actual code and push to GitHub.
- Heroku was used to deploy the application
- PostgreSQL was used as database


## Code Validation
---
### HTML Validation
All code of all rendered HTML pages of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/). 

The errors that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### CSS Validation
All CSS files of the project have been validated by [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

No errors raised.

### Python Validation
All Python files of the project were formatted by [Black Code Formatter](https://black.vercel.app/). (PEP8 Standard)

No errors raised.

## Tests
---
### Lighthouse
![Screenshot Lighthouse](/static/images_readme/screenshot_lighthouse.PNG)


### Manual Tests
Currently, only 2 views (ArticleList, home_view )from views.py of the wiki app are tested. 
These test are located in test.py. The remaining 7 tests for the views will be published in the next deployment cycle.


## Bugs
---
### Solved
I fixed a bug that occurred when replacing or editing an article without filling in the title field. 
This was fixed by form validation.

### Unsolved
No unsolved bugs.


## Deployment
---
Steps to deploy on Heroku:

- START A BASIC DJANGO PROJECT

- Use CI Full Template

- Install libraries etc. for basic functionality: pip3 install (“django<4”-(framework), gunicorn-(WSGI, Server to run Django on Heroku), dj_database_url==0.5.0-(for Heroku DB), psycopg2-(DB Adapter for PostgresSQL), dj3-cloudinary-storage-(stores our images and static files)).

- Create requirements.txt: pip3 freeze –local > requirements.txt

- Start django project: django-admin startproject yourProjectName .

- Create django app: python3 manage.py startapp yourAppName

- Add your new App to App list in settings.py: yourProjectName/settings.py > INSTALLED_APPS add “yourAppName”, to list

- Migrate Changes to DB: python3 manage.py migrate (now you can use python3 manage.py runserver to check if everything works) 
    
- Create new heroku app

- In Resources tab add Heroku PostgresSQL to project

- In Setting tab > Config Vars copy DATABASE_URL string

- Create env.py: add
import os
os.environ[“DATABASE_URL”] = “yourDatabaseUrl”
os.environ[“SECRET_KEY”] = “randomSecretKey123?” 


- Copy SECRET_KEY value & add to Heroku Config Vars

- In settings.py: 
import os
import dj_database_url
if os.path.isfile(“env.py”):
    import env
} {
SECRET_KEY = os.environ.get(“SECRET_KEY”)
} *Comment out DATABASES variable & add* {
DATABASES = {
“default”: dj_database_url.parse(os.environ.get(“DATABASE_URL”))
}


- Migrate again: python3 manage.py migrate

- In Heroku Resources tab, click on Heroku Postgres link: check rows and tables

- Copy Cloudinary API Environment variable

- In env.py: add 
os.environ[“CLOUDINARY_URL”] = (delete CLODINARY_URL=)“pasteHere” 


- In Heroku Config Vars add: CLOUDINARY_URL = (delete CLODINARY_URL=)“pasteHere” 

- In Heroku Config Vars add: DISABLE_COLLECTSTATIC = 1

- In Heroku Config Vars add: PORT= 8000

- In settings.py > # Application definition > INSTALLED_APPS: {
“cloudinary_storage”,
“django.contrib.staticfiles”,
“cloudinary”,
}

- In settings.py > # Static files: 
STATICFILES_STORAGE = 'clodinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


- In settings.py underneath BASE_DIR create: TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

- In settings.py in the TEMPLATES variable change: 'DIRS': [TEMPLATES_DIR],

- In settings.py in the ALLOWED_HOSTS variable add: [yourHerokuAppName.herokuapp.com', 'localhost']

- Create media, static, templates folders on top level next to manage.py

- Create Procfile on top level & add: web: gunicorn yourDjangoProjectName.wsgi

- Deploy to GitHub: git add . > git commit -m “yourDeploymentMessage” > git push

- In Heroku Deploy Tab click GitHub as Deployment method, connect repo & click Deploy Branch

- Before final deployment: In settings.py set DEBUG = False & create X_FRAME_OPTIONS = 'SAMEORIGIN'

## Credits
---
No Credits so far.