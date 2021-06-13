Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)

Disclaimer: Much of this code has been inspired from UIS_bank which has been downloaded from absalon and provided by our Professor, Dmitriy Traytel. 

The core idea of 'Volt' has also originally been provided by Dmitriy Traytel, where we have made our own interpretation of how the app should work, which has also been described in Assignment 1 of our course, 'Databaser og informationssystemer'.

Furthermore, we expect you to have a working installation of PostgreSQL, if not, it can be downloaded from: https://www.postgresql.org/
also make sure that you have the following python modules: flask, flask_bcrypt, flask_login, flask_wtf, wtforms and psycopg2


Step by step guide
    1. Set up your database:
        1.1 Open your terminal
        1.2 Start PostgreSQL in your terminal by typing: 'psql' or 'psql -pPORTNR' where PORTNR = your own portnumber (usually: 5432)
        1.3 Create a new database (CREATE DATABASE volt;) and call it "volt" (otherwise you have to change the 'dbname' in __init__.py)
        1.4 Open a new terminal and navigate to the folder 'volt'
        1.5 Start PostgreSQL again but now type: psql -pPORTNR "volt"
        1.6 Run following: \i tables.sql
        1.7 At last run: \i data.sql

    2. Set up the file '__init.py':
        2.1 Open the file '__init.py'
        2.2 Make sure that your database name is the same as 'dbname' otherwise change it
        2.3 Make sure that your portnumber is the same as 'port' otherwise remove port='5420' (if you don't use a portnumber) or change it
        2.4 DO NOTE: 'user' and 'password' are set to 'postgres'. Remember to change it if you don't have this user and password
    
    3. Start the application:
        3.1 Open a new terminal and navigate to the folder 'Project'
        3.2 Run following: python run.py
        3.3 Copy: http://127.0.0.1:5000/ (the URL) and past it in a browser
        3.4 You should now be at our Homepage

    4. How to login:
        4.1 To log in as a Customer see the existing Customers in our database (data.sql) where you can find usernames and passwords in the table 'Customers'
        4.2 To log in as a Restaurant and/or Courier see the existing Restaurants/Couriers in our database (data.sql) where you can find usernames and passwords as 'name' and 'base' in the table Restaurants/Couriers, respectively
        4.3 DO NOTE: To distinguish Customers, Restaurants and Couriers, we have made it so that Restaurants have the prefix 'VRES-' and Couriers have 'VCOU-' as prefixes to their actual name/ID, respectively. Customers have no prefix.
    
    5. How to sign up as a Customer:
        5.1 Navigate to the Customer login page and press: 'Sign up'
        5.2 Enter the fields with information described next to each text input box
        5.3 Press 'Add'
        5.3 You should now be at the Customer login page where you can log in with the created user
    
    6. How to make a food order as a Customer:
        6.1 After you're logged in as a Customer pick a meal and remember to select if want as take-out (orders are delivered by default)
        6.2 Press 'Add'
        6.3 You should now be able to see your order(s)
        6.4 You can make a new order by pressing 'Make a new order'


Description of the HTML pages
    - homepage: Homepage of the website, shows the 3 login buttons for Customer, Restaurant and Courier.

    - courierLogin: Login page of Courier.
    - customerLogin: Login page of Customer.
    - restaurantLogin: Login page of Restaurant.

    - customerAdd: Page where you can sign up a new Customer.
    - customerHomepage: Page where the Customer selects order and whether said Customer picks up the order him/herself.

    - courierOrders: Page where logged in Couriers can see the what orders they have to deliver and the ratings they received.
    - restaurantOrders: Page where logged in Restaurants can see the what orders they have to make and the ratings they received, also whether or not they are delivery or takout orders.
    - customerOrders: Page where logged in Customers can see the what orders they have ordered, and whether they are delivery or takout.


Description of SQL tables
    - United_contracts: Used to link tables in our queries. Initially used for setting up a zone for United orders to be realized, but we ended up scrapping it due to time constraint.
    - Customers: Keeps the Customers and their info.
    - Couriers: Keeps the Couriers and their info.
    - Restaurants: Keeps the Restaurants and their info.
    - Meal_combinations: Keeps meals and meal combinations.
    - Food_orders: Keeps food orders, including order number, who made it, what is ordered and when it is ordered, etc.
    - Take_out_orders: Keeps the time it is expected to be picked up, default set to 30 min after order placement.
    - Courier_orders: Keeps the time it is expected to be delivered, default set to 30 min after order placement.
    - Cus_rates_Res: Restaurant ratings from Customer.
    - Cus_rates_Cour: Courier ratings from Customer.
    - Makes: Keeps which Restaurants that make which meals.
    - Receives: Keeps orders and what Couriers have to deliver to what Customers.
