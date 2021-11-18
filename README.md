# Milestone-Project-3
My third Code Institute milestone project concerning Backend Development.

## Purpose of the website

### Who is this website for?
This is a website for people wanting to look up and share recipes. 
It should be user friendly such that the customer can easily access other people's recipes and share their own with ease.

### What does it do?
The user can use full CRUD functionality to create, update and delete your recipe on the website, while anyone on the website can read the posted recipes.


### User Experience Design

#### User Stories

##### As a first time visitor:
- As a first time visitor, I want to easily navigate this website
- As a first time visitor, I want there to be recipes that have information about the dish
- As a first time visitor, I want to be able to use the website comfortably on any of my devices
##### As a returning visitor:
- As a returning visitor, I want to be able to access more information about the recipes easily
- As a returning visitor, I want the website to be intuitive 
- As a returning visitor, I want to be able to create an account to post recipes
##### As a frequent visitor
- As a frequent visitor, I want to be able to update and delete my own recipes within the website easily
- As a frequent visitor, I want to be able to quickly log in to my account to access the CRUD functionalitites of the website
#### Structure
The website is contained within multiple html pages, which all extend from base.html. The navbar is constant across pages when logged in or logged out, and is collapsible at smaller screen sizes. The purpose of this is to fulfill user stories:
> As a first time visitor, I want to easily navigate this website

> As a first time visitor, I want to be able to use the website comfortably on any of my devices

> As a returning visitor, I want the website to be intuitive 

In the recipes page, there are collapsible elements which open to show more information on each recipe. The purpose of this is to fulfill user stories:
> As a first time visitor, I want there to be recipes that have information about the dish

> As a returning visitor, I want to be able to access more information about the recipes easily

In the add page, there are multiple fields that operate with a dropdown choice. The purpose of this is to fulfill user story:
> As a returning visitor, I want the website to be intuitive

There is a Register and a Log In page available in the navbar
> As a returning visitor, I want to be able to create an account to post recipes

> As a frequent visitor, I want to be able to quickly log in to my account to access the CRUD functionalitites of the website

In the recipes page, a user can edit and delete recipes that they have added. The purpose of this is to fulfill user story:
> As a frequent visitor, I want to be able to update and delete my own recipes within the website easily

#### Design and Wireframes

##### Colour scheme
I used aspects of a colour scheme from the featured section of coolers. The background of the website is white as standard, with the nav and collapsible elements being charcoal: #264653ff, buttons and other interactive elements as persian green: #2a9d8fff and the background of the collapsible elements' bodies being thistle: #D8BFD8 to contrast with the flags in the body.

##### Typography
I have used Alegreya for the full website, across the navbar and the body.

##### Images
I used no images across this website, only using [Flag-icons](https://flagicons.lipis.dev/) and [Fontawesome](https://fontawesome.com/) for icons within the website.

##### Wireframes
Wireframes are linked here:


- [Register Page](/wireframes/register.png)



- [Login Page](/wireframes/login.png)


- [Add Recipe Page](/wireframes/add_recipe.png)


- [Browse recipe Page](/wireframes/browse_recipes.png)

To access these wireframes seperately, click the links below:
* [Register wireframes](/wireframes/register.png)
* [Login wireframes](/wireframes/login.png)
* [Add Recipe wireframes](/wireframes/add_recipe.png)
* [Browse Recipe wireframes](/wireframes/browse_recipes.png)
##### Divergences from my wireframes
The main divergence from my wireframes is that I have a message in the left of the navbar shwoing the session user's username. Other than that, the project is relatively close to how the wireframes predict.
# Features

## Existing Features

### CRUD operation
- Can Create by using the add function in the Add a Recipe page
- Can Read through the Recipe page
- Can Update by pressing the edit button on your own recipe in the Recipe page
- Can Delete by pressing the delete button on your own recipe in the Recipe page

## Technologies
* HTML
    * This project uses HTML for the structure and content of the site.
* CSS
    * This project uses a custom CSS file to style the site.
* JS
    * This project uses custom JS files to add functionality to the site.
* Python
    * This project uses a custom python to add functionality to the site and in the HTML files to extend functionality, structure and content.
* [Materialize](https://materializecss.com/)
    * This project uses Materialize CSS and JS to style the site and add layout and various functionalities such as buttons.
* [Google Fonts](https://fonts.google.com/)
    * This project uses Google fonts to style the text in the site.
* [Flag-icons](https://flagicons.lipis.dev/)
    * This project uses flag-icons to add flag icons to the project.
* [Fontawesome](https://fontawesome.com/)
    * This project uses fontawesome to add icons to the project.
* [Balsamiq Wireframes](https://balsamiq.com/wireframes/?gclid=CjwKCAiA9bmABhBbEiwASb35Vz5eNriDRNqnP0yfLYeqI0aYF9r5Qf45QNEoXootlZ-VmwSloDl8rRoCdbcQAvD_BwE)
    * Balsamiq Wireframes were used to create wireframes for UX design.
* [Github](https://github.com/)
    * This project uses Github as the hosting site, which stores the code.
* [Coolors](https://coolors.co/)
    * This project uses a colour scheme made from the featured colour schemes on coolers.
* [Jquery](https://jquery.com/)
    * Jquery is used in this project as a method of adding functionality in the js file.
* [Mongodb](https://www.mongodb.com/)
    * Mongodb is used in this project to add content (recipes page) and functionality (login/register and CRUD functionality)
* [Heroku](https://www.heroku.com)
    * Heroku is used for the deployment of this app.

## Testing and Bug Fixes
### Code Validation

#### HTML
All HTML files have been run through the W3C Markup Validation Service; this service has given a few errors.
- Error: Bad value has been given for lines containing urls, which is a consequence of using flask and can be ignored.
- Error: Stray End Tag/ Start tag seen but an element of the same type was already open have both been given for base.html head and body tags.
Each of these have been checked against the code and have only one ninstance despite the error.
- Error: Text not allowed in element in this context has been given; this error is a consequence of using python in html and can be ignored.


#### CSS
style.css has been run through the W3C CSS Validation Service, giving no errors or warnings.

#### Javascript
script.js has been run through [JSHint](https://jshint.com/) and no warnings were given.
There is 1 undefined variable: $, which is used in jquery and thus can be ignored.

#### Python
app.py has been run through [Extends Class Python Tester](https://extendsclass.com/python-tester.html) and returned no errors.
app.py has also been tested using python3 -m flake8 in the terminal, which returns 2 errors:
- ./app.py:9:5: F401 'env' imported but unused; which is unused as I have set variables in my gitpod and heroku settings and can be ignored.
- ./app.py:23:1: E304 blank lines found after function decorator; which I cannot find the reason for, as there is no blank line found after and the function decorator is formatted the same as all others which did not return this error.

### Browser Testing
As this is a backend oriented project, the testing will have a large emphasis on functionality while also having to maintain layout and responsiveness to changes in screen size.
Testing will be done across google chrome, mozilla firefox and microsoft edge at small (phone), medium (tablet/notebook) and large (any larger screen) sizes.


To be considered successful, in each browser and at each size the webpage should;
- Contain working and correct hyperlinks, both internal and external, with external links opening in a fresh tab.
- Have no overlapping divs/ sections such that the layout is compromised.
- Display a similar layout as to the wireframes provided above, with the exception of changes in layout design mentioned alongside the wireframes.

| Test Description  	|   Shorthand Reference	|
|---	|---	|
|   Layout should be preserved at all window sizes	|  TC1 	|
|  Register a user	|   TC2 |
|  Logout of the user 	|   TC3 |
|  Login to the user 	|   TC4	|
|  Add a recipe	|   TC5	|
|  Edit a recipe	|   TC6	|
|  Delete a recipe 	|   TC7	|

#### TC1

Testing process:
- Open website in the tested browser
- Right click and inspect element
- Change device width for each size class (small, medium and large)

Test case results for each browser:
- Google chrome - Testing all 3 size classes, the webpage acted as desired and passed.
- Microsoft edge - Testing all 3 size classes, the webpage acted as desired and passed.
- Mozilla firefox - Testing all 3 size classes, the webpage acted as desired and passed.

#### TC2
Testing process:
- Open website in the tested browser
- Register a user through register.html

Test case results for each browser:
- Google chrome - Registered user google and gained access to the blocked part of the website, passed.
- Microsoft edge - Registered user edge1 and gained access to the blocked part of the website, passed.
- Mozilla firefox - Registered user firefox and gained access to the blocked part of the website, passed.

#### TC3
Testing process:
- Open website in the tested browser
- Logoutfrom the user using the logout link in the navbar

Test case results for each browser:
- Google chrome - Logged out from user google successfully.
- Microsoft edge - Logged out from user edge1 successfully.
- Mozilla firefox - Logged out from user firefox successfully.

#### TC4
Testing process:
- Open website in the tested browser
- Login as a user through login.html

Test case results for each browser:
- Google chrome - Logged in to user google successfully.
- Microsoft edge - Logged in to user edge1 successfully.
- Mozilla firefox - Logged in to user firefox successfully.

#### TC5
Testing process:
- Open website in the tested browser
- Add a recipe through add.html
- Check the recipe is correct through recipe.html and the mongodb database

Test case results for each browser:
- Google chrome - Added a recipe which can be seen in recipe.html and mongodb
- Microsoft edge - Added a recipe which can be seen in recipe.html and mongodb
- Mozilla firefox - Added a recipe which can be seen in recipe.html and mongodb

#### TC6
Testing process:
- Open website in the tested browser
- Edit a recipe through edit.html
- Check the recipe is correct through recipe.html and the mongodb database

Test case results for each browser:
- Google chrome - Edited the recipe which can be seen as changed in recipe.html and mongodb
- Microsoft edge - Edited the recipe which can be seen as changed in recipe.html and mongodb
- Mozilla firefox - Edited the recipe which can be seen as changed in recipe.html and mongodb

#### TC7
Testing process:
- Open website in the tested browser
- Delete a recipe through the delete button in recipe.html
- Check the recipe is deleted through recipe.html and the mongodb database

Test case results for each browser:
- Google chrome - Deleted the recipe and it cannot be seen in recipe.html or mongodb
- Microsoft edge - Deleted the recipe and it cannot be seen in recipe.html or mongodb
- Mozilla firefox - Deleted the recipe and it cannot be seen in recipe.html or mongodb

#### Notable bug fixes during coding and testing
- Before my testing session, I had difficulty displaying the edit.html page which was easily fixed with a small change to the python code rendering the template.
- Before my testing session, I had difficulty displaying the dropdown fields in add.html and edit.html, which was simply a typing error inside the option value for each one.

## Version Control

### Github
This project was created in its own repository using Github under my account name. It is named Willdeakin/Milestone-Project-3, and all pushed files can be seen here.

I used Gitpod to write and edit these files, using the bash terminal for saving, updating and version control of the project. For the purpose of this project, I used these commands:
- git add -A; to add all files to the staging area
- git commit -m "*message detailing the changes from the last version*"; to commit changes from the staging area to the local repository
- git push; to push committed changes from the local repository to the Github repository

## Deployment

For project deployment I used [Heroku](https://www.heroku.com/), a cloud platform where users can host their projects.
For the purpose of this project the free version was suitable.
All of the files were pushed to Heroku for this deployment.

Heroku setup:
- I created a new app by clicking on *New* and then *Create new app*
- I named the new app milestone-project-3-willdeakin and chose the region europe

Steps I took before deployment:

- I froze all requirements using pip3 freeze > requirements.txt so that Heroku could load all dependencies upon deployment
- I created a Procfile such that Heroku knows the necessary details to deploy correctly

Before enabling automatic deploys, I had to set Config Vars in settings for the Mongo DB Name, URI etc.
After adding all the necessary Config Vars, I enabled automatic deploys such that every subsequent push in my linked GitHub would push to Heroku also.
- Every time the app deploys, this is seen in the Activity tab.

### Accessing the Project Through Heroku
- Access the Project using Heroku [here](https://milestone-project-3-willdeakin.herokuapp.com/)
 
## Credits
- Code
    - The main structure of the app.py and base.html is inspired by the task manager mini project
    - Lines 160-168 of app.py are from [askpython](https://www.askpython.com/python-modules/flask/flask-error-handling)
    - The code of this project was created by Will Deakin.

- Content
    - The content of this project was created by Will Deakin.

Thanks to my mentor Spencer Barriball for feedback and guidance for this project, which lead me in good stead.