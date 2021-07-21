# Milestone-Project-3
My third Code Institute milestone project concerning  Backend Development

## Table Of Contents
* [Purpose of the website](#purpose-of-the-website)
* [User Experience (UX)](#user-experience-design)
    * [User Stories](#user-stories)
    * [Structure](#structure)
    * [Design and Wireframes](#design-and-wireframes)
* [Features](#features)
* [Technologies](#technologies)
* [Testing and Bug Fixes](#testing-and-bug-fixes)
* [Deployment](#deployment)
    * [Project Creation](#project-creation)
    * [Heroku](#using-heroku)
    * [Locally](#run-locally)
* [Credits](#credits)

## Purpose of the website

### User Experience Design
#### User Stories

##### As a first time visitor:
- As a first time visitor, I want to easily navigate this website
- As a first time visitor, I want there to be recipes that have information about the dish
- As a first time visitor, I want to be able to use the website comfortably on any of my devices
##### As a returning visitor:
- As a returning visitor, I want to be able to access more information about the recipes easily
- As a returning visitor, I want the website to be intuitive 
##### As a frequent visitor
- As a frequent visitor, I want to be able to perform CRUD operations on my own recipes within the website easily
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

> As a frequent visitor, I want to be able to perform CRUD operations on my own recipes within the website easily

In the recipes page, a user can edit and delete recipes that they have added. The purpose of this is to fulfill user story:
> As a frequent visitor, I want to be able to perform CRUD operations on my own recipes within the website easily




#### Design and Wireframes

##### Colour scheme
I used aspects of a colour scheme from the featured section of coolers. The background of the website is white as standard, with the nav and collapsible elements being charcoal: #264653ff, buttons and other interactive elements as persian green: #2a9d8fff and the background of the collapsible elements' bodies being thistle: #D8BFD8 to contrast with the flags in the body.

##### Typography
I have used Alegreya for the full website, across the navbar and the body.

##### Images
I used no images across this website, only using [Flag-icons](https://flagicons.lipis.dev/) and [Fontawesome](https://fontawesome.com/) for icons within the website.

##### Wireframes
Register Page

![My register wireframes](/wireframes/register.png)

Login Page

![My login wireframes](/wireframes/login.png)

Add Recipe Page

![My add recipe wireframes](/wireframes/add_recipe.png)

Browse recipe Page

![My browse recipe wireframes](/wireframes/browse_recipes.png)

To access these wireframes seperately, click the links below:
* [Register wireframes](/wireframes/register.png)
* [Login wireframes](/wireframes/login.png)
* [Add Recipe wireframes](/wireframes/add_recipe.png)
* [Browse Recipe wireframes](/wireframes/browse_recipes.png)
##### Divergences from my wireframes
The main divergence from my wireframes is that I have a message in the left of the navbar shwoing the session user's username. Other than that, the project is relatively close to how the wireframes predict.
# Features

### Features I Would Have Liked To Implement

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

#### Notable bug fixes during coding and testing
- Before my testing session, I had difficulty displaying the edit.html page which was easily fixed with a small change to the python code rendering the template.

## Deployment

### Project Creation
This project was created in its own repository using Github under my account name. It is named Willdeakin/Milestone-Project-3, and all pushed files can be seen here.

### Heroku


## Credits
- Code
    - The code of this project was created by Will Deakin.

- Content
    - The content of this project was created by Will Deakin.


Thanks to my mentor Spencer Barriball for feedback and guidance for this project, which lead me in good stead.