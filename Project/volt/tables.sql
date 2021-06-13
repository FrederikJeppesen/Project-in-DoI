--Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
\i droptables.sql


CREATE TABLE IF NOT EXISTS United_contracts(zone INTEGER, PRIMARY KEY (zone));

CREATE TABLE IF NOT EXISTS Customers(base varchar(120), password varchar(120), username varchar(120), zone INTEGER, PRIMARY KEY(username));

CREATE TABLE IF NOT EXISTS Couriers(capacity INTEGER, base varchar(120), courier_id varchar(120), zone INTEGER, PRIMARY KEY(courier_id), FOREIGN KEY(zone) REFERENCES United_contracts);

CREATE TABLE IF NOT EXISTS Restaurants(base varchar(120), name varchar(120), zone INTEGER, PRIMARY KEY(base, name), FOREIGN KEY(zone) REFERENCES United_contracts);

CREATE TABLE IF NOT EXISTS Meal_combinations(meal_name varchar(120), price FLOAT, is_united INTEGER, nr_of_dishes INTEGER, zone INTEGER, PRIMARY KEY(meal_name, price, nr_of_dishes), FOREIGN KEY(zone) REFERENCES United_contracts);

CREATE TABLE IF NOT EXISTS Food_orders(order_nr INTEGER, time_of_order varchar(120), meal_name varchar(120), price FLOAT, nr_of_dishes INTEGER, username varchar(120), PRIMARY KEY(order_nr), FOREIGN KEY(username) REFERENCES Customers, FOREIGN KEY(meal_name, price, nr_of_dishes) REFERENCES Meal_combinations);

CREATE TABLE IF NOT EXISTS Take_out_orders(order_nr INTEGER, pick_up_time varchar(120), PRIMARY KEY(order_nr), FOREIGN KEY(order_nr) REFERENCES Food_orders);

CREATE TABLE IF NOT EXISTS Courier_orders(order_nr INTEGER, eta varchar(120), PRIMARY KEY(order_nr), FOREIGN KEY(order_nr) REFERENCES Food_orders);


CREATE TABLE IF NOT EXISTS Cus_rates_Res(username varchar(120), base varchar(120), name varchar(120), rate INTEGER, PRIMARY KEY(username, base, name), FOREIGN KEY(username) REFERENCES Customers, FOREIGN KEY(base, name) REFERENCES Restaurants);

CREATE TABLE IF NOT EXISTS Cus_rates_Cour(username varchar(120), courier_id varchar(120), rate INTEGER, PRIMARY KEY(username, courier_id), FOREIGN KEY(username) REFERENCES Customers, FOREIGN KEY(courier_id) REFERENCES Couriers);

CREATE TABLE IF NOT EXISTS Makes(name varchar(120), base varchar(120), meal_name varchar(120), price FLOAT, nr_of_dishes INTEGER, PRIMARY KEY(name, base, meal_name, price, nr_of_dishes), FOREIGN KEY(base, name) REFERENCES Restaurants, FOREIGN KEY(meal_name, price, nr_of_dishes) REFERENCES Meal_combinations);

CREATE TABLE IF NOT EXISTS Receives(order_nr INTEGER, name varchar(120), base varchar(120), courier_id varchar(120), PRIMARY KEY(order_nr, name, base, courier_id), FOREIGN KEY(order_nr) REFERENCES Food_orders, FOREIGN KEY(courier_id) REFERENCES Couriers, FOREIGN KEY(base, name) REFERENCES Restaurants);
