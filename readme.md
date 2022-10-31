# NATURAL HEALING WIKI
![Screenshot of the website](/static/images_readme/screenshot_responsiveness.PNG)

Natural Healing Wiki is a web application that is operated similarly to a normal wiki. 

The purpose of the application is to share knowledge about natural healing in the form of informative articles and allow users to create new contributions.

Users can view articles written by other users or administrators and create their own articles. However, only own articles can be edited. Before publication, articles created by users must be checked by administrators for appropriate content and then authenticated.

Click [here](https://natural-healing-wiki.herokuapp.com/) to live site.

## User Stories
---

GitHub issues was used to document user stories. 
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

### User Stories for next relese
- As a Site User, I can leave comments on an article, so that I can share my opinion about this article with others.
- As a Site User, I can view the comments of a specific article, so that I can read the added comments.
- As a Side Admin, I can approve or disapprove comments written by users, so that I can filter out faulty or unsuitable comments.
- As a Site User, I can view different categories and choose from them, so that I can view the associated articles.
- As a Site User, I can choose a category for my written article, so that my article gets assigned a category.
- As a Site User / Admin, I can create draft articles, so that I can finish writing the content later.

## Agile Methodology
---
![Screenshot of the website](/static/images_readme/screenshot_userstories.PNG)

MoSCoW priority setting was used to create an agile project via GitHub Issues. 

Link to the project with live issues can be found [here](https://github.com/users/LucaNoah/projects/8).


## Wireframes
---

## Existing Features
---
### - Navbar
On the left side, the logo is displayed with a link to the home page. Next to it, you can navigate to all articles or the articles created by the logged-in user via a drop-down menu. Further to the right is the navigation element for creating a new article. This element is only linked if the user is logged in. If the user is not logged in, its unusability is represented by a visual missing function. Even further to the right are the options to register or log in. If you are already logged in, logout is displayed there. On the far right are 2 social media icons that are connected to a link to the respective website that opens in a new window.

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
In the same dropdown menu as all articles, there is a navigation named "Your Articles" which leads to a page that displays all articles of the currently logged in user in chronological order.

### - Article Detail
By pressing the "Read" button below an article, the user is redirected to the corresponding article. The title, the name of the author, the date of creation, the description and the content are displayed. If the logged-in user is the author, the buttons "Edit" and "Delete" are visible at the very end.

### - Create Article
On this page logged in users can write articles. To do this, you are required to enter a title, description and related content. The Author field is automatically filled in based on the username. The author will be informed that his article will be styled and authenticated before publishing. He will also be asked to provide references if necessary. If Create is pressed, the user is asked again via modal whether his interaction should be carried out.

### - Edit Article
At the bottom of the article detail page, if the logged in user is also the author, the "Edit" button is displayed. This will take the user to a page to edit the associated article. The page is built the same as the page to create an article, with the difference that the fields with the related information are prefilled.

### - Form Validation
When the user fills in the form to create or edit, it is validated by HTML attributes. 
The user cannot submit empty fields and is limited in the length of the characters.

### - Delete Article
At the bottom of the article detail page, if the logged in user is also the author, the "Delete" button is displayed. With this button the user can delete the article from the database after validating the request via modal.

### - Approve article
As an admin, articles written by users can be authenticated via the admin panel. 
Only then will they be displayed on the website.

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
### HTML Valiation
All code of all rendered HTML pages of the project was validated by the [W3C Markup Validation Service](https://validator.w3.org/). 

The errors that occur there cannot be avoided and do not affect the function of the app. They can be considered irrelevant.

### CSS Valiation
All CSS files of the project have been validated by [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/).

No errors raised.

### Python Validaton
All Python files of the project were formatted by [Black Code Formatter](https://black.vercel.app/). (PEP8 Standart)

No errors raised.

## Tests
---


## Bugs
---

## Deployment
---

## Credits
---