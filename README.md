# Grocery List Management System - Bread and Butter
Welcome to the simple Grocery List Management System, a project developed while being a CodeClan student! Originally, the task was to create an order management system for a takeaway, but I decided to adapt the project to create a grocery list management system that meets the same criteria.

## Project Overview
The Grocery List Management System allows users to create and manage their grocery lists. Each list can contain various grocery items with their names and prices. The system is designed to help users keep track of their shopping needs and efficiently manage their grocery lists.

## Goals
 * Option to create a new user
 * Users can create multiple grocery lists with multiple items on each of them
 * Each grocery item in the list includes a name and a price, enabling accurate budgeting.
 * The system provides a user-friendly page to view all grocery lists, and users can click through to see the details of each list.
 * Users have the option to edit or delete grocery lists as needed, providing flexibility and control.

## Technologies used
[![My Skills](https://skillicons.dev/icons?i=python,flask,css,html,postgresql)](https://skillicons.dev)


### Features

**Create Grocery Lists: Easily create new grocery lists for chosen user, add grocery items with names and prices**

**View All Grocery Lists: Access a page displaying all existing grocery lists.**

**View Details: Click on any grocery list to view its detailed information, including total value of all items on the list and individual grocery items.**

**Edit and Delete: Users can edit the contents of a grocery list or delete it entirely, offering flexibility in managing their shopping needs.**

**Update or Delete Items: If you need to add more items in a list or remove it altogether, the system allows you to easily make those changes.**

## Getting Started

1. Clone the repository to your local machine.

2. Set Up Database: Before running the project, ensure you have PostgreSQL installed and running. In app.py, change the name of the database to whatever you want to name it.

3. Create Database: Open your terminal and run createdb your_name to create the database.

4. Initialize Database: Run flask db init to initialize the database.

5. Migrations: Utilize Flask's migration tool to set up the database schema by running flask db migrate followed by flask db upgrade.

6. Populate Database (Optional): If you want to use the provided dummy data to play around, run flask seed to populate the database.

7. Run the Application: To start the application, run flask run in the terminal. The application will be accessible at http://localhost:4999/.
    Note: If port 4999 is blocked on your machine, you can change the port number in the .flaskenv file located in the root directory of the project.

#### Thank you for using Bread & Butter, grocery list management system. I hope you will enjoy this simple system. Happy shopping! 🛒🛍️🛒🛍️







Regenerate