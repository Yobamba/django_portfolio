# django_portfolio
# Overview

Creating a portfolio of my projects using Django. The purpose is to learn Django while also creating a portfolio that I will use. 

# Running the code
Open the terminal and use the "python manage.py runserver" command. Then open http://127.0.0.1:8000/ to view the portfolio. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](https://youtu.be/W9JLtfzM9Jo)

# Web Pages

{Describe each of the web pages you created and how the web app transitions between each of them.  Also describe what is dynamically created on each page.}

Pages Created
* Home page. This is where I show the projects from my portfolio. It contains a list of projects with screenshots and descriptions. On each project there's a short description of what the project is as well as a read more link that when clicked takes the user to the Project Details page to see more details on the selected project. Images and project details are stored in sqlite db. 
* Project Details page. Contains the screenshot and the full details of the selected project. 
* About Me page. Contains information about me. The link to this page is found on every page because it is a part of the base template that I'm using thanks to Django. 

# Development Environment

Tools used: 
* Python
* VS Code
* Django
* Sqlite3

# Languages & Framework

Languages: 
* Python
* JavaScript
* HTML5
* CSS

Framework: Django

# Useful Websites

* [Django Docummentation](https://docs.djangoproject.com/en/5.0/)
* [Tutorials Point](https://www.tutorialspoint.com/django/index.htm)

# Future Work

Things that I need to fix, improve, and add in the future: 
* Add more projects
* Host it online
* Clean out the code by removing redundancies and more