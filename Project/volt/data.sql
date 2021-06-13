--Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)

DELETE FROM customers;
DELETE FROM united_contracts;
DELETE FROM meal_combinations;
DELETE FROM food_orders;
DELETE FROM restaurants;
DELETE FROM couriers;
DELETE FROM courier_orders;
DELETE FROM receives;
DELETE FROM makes;
DELETE FROM cus_rates_res;
DELETE FROM cus_rates_cour;


INSERT INTO public.customers(base, password, username, zone) VALUES ('Herlev', '1234', 'Frederik2730', 1);
INSERT INTO public.customers(base, password, username, zone) VALUES ('Virum', '5678', 'Patrick2830', 3);
INSERT INTO public.customers(base, password, username, zone) VALUES ('Herlev', 'abcd', 'Aage2730', 1);
INSERT INTO public.customers(base, password, username, zone) VALUES ('Virum', 'efgh', 'Bent2830', 3);

INSERT INTO public.united_contracts(zone) VALUES (1);
INSERT INTO public.united_contracts(zone) VALUES (3);

INSERT INTO public.meal_combinations(meal_name, price, nr_of_dishes, zone) VALUES ('Big_Mac', 25.0, 1, 1);
INSERT INTO public.meal_combinations(meal_name, price, nr_of_dishes, zone) VALUES ('Hawaii', 65.0, 1, 1); 
INSERT INTO public.meal_combinations(meal_name, price, nr_of_dishes, zone) VALUES ('Cheese_Burger', 10.0, 1, 3);
INSERT INTO public.meal_combinations(meal_name, price, nr_of_dishes, zone) VALUES ('Pepperoni', 60.0, 1, 3);

INSERT INTO public.food_orders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username) VALUES (0, '2021-06-09 17:23:13', 'Big_Mac', 25.0, 1, 'Frederik2730');
INSERT INTO public.food_orders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username) VALUES (1, '2021-06-08 16:43:58', 'Hawaii', 65.0, 1, 'Aage2730');
INSERT INTO public.food_orders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username) VALUES (2, '2021-06-09 17:42:19', 'Cheese_Burger', 10.0, 1, 'Patrick2830');
INSERT INTO public.food_orders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username) VALUES (3, '2021-06-08 18:14:27', 'Pepperoni', 60.0, 1, 'Bent2830');

INSERT INTO public.restaurants(base, name, zone) VALUES ('Herlev', 'VRES-McDonalds', 1);
INSERT INTO public.restaurants(base, name, zone) VALUES ('Herlev', 'VRES-Farfars', 1);
INSERT INTO public.restaurants(base, name, zone) VALUES ('Virum', 'VRES-McDonalds', 3);
INSERT INTO public.restaurants(base, name, zone) VALUES ('Virum', 'VRES-Bellini', 3);

INSERT INTO public.couriers(capacity, base, courier_id, zone) VALUES (5, 'Herlev', 'VCOU-10', 1);
INSERT INTO public.couriers(capacity, base, courier_id, zone) VALUES (8, 'Virum', 'VCOU-4', 3);

INSERT INTO public.courier_orders(order_nr, eta) VALUES (0, '2021-06-09 17:23:13');
INSERT INTO public.courier_orders(order_nr, eta) VALUES (1, '2021-06-08 16:43:58');
INSERT INTO public.courier_orders(order_nr, eta) VALUES (2, '2021-06-09 17:42:19');
INSERT INTO public.courier_orders(order_nr, eta) VALUES (3, '2021-06-08 18:14:27');

INSERT INTO public.receives(order_nr, name, base, courier_id) VALUES (0, 'VRES-McDonalds', 'Herlev', 'VCOU-10');
INSERT INTO public.receives(order_nr, name, base, courier_id) VALUES (1, 'VRES-Farfars', 'Herlev', 'VCOU-10');
INSERT INTO public.receives(order_nr, name, base, courier_id) VALUES (2, 'VRES-McDonalds', 'Virum', 'VCOU-4');
INSERT INTO public.receives(order_nr, name, base, courier_id) VALUES (3, 'VRES-Bellini', 'Virum', 'VCOU-4');

INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-McDonalds', 'Herlev', 'Big_Mac', 25.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-McDonalds', 'Herlev', 'Cheese_Burger', 10.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-Farfars', 'Herlev', 'Hawaii', 65.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-Farfars', 'Herlev', 'Pepperoni', 60.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-McDonalds', 'Virum', 'Big_Mac', 25.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-McDonalds', 'Virum', 'Cheese_Burger', 10.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-Bellini', 'Virum', 'Hawaii', 65.0, 1);
INSERT INTO public.makes(name, base, meal_name, price, nr_of_dishes) VALUES ('VRES-Bellini', 'Virum', 'Pepperoni', 60.0, 1);

INSERT INTO public.cus_rates_res(username, base, name, rate) VALUES ('Frederik2730', 'Herlev', 'VRES-McDonalds', 2);
INSERT INTO public.cus_rates_res(username, base, name, rate) VALUES ('Aage2730', 'Herlev', 'VRES-Farfars', 8);
INSERT INTO public.cus_rates_res(username, base, name, rate) VALUES ('Patrick2830', 'Virum', 'VRES-McDonalds', 5);
INSERT INTO public.cus_rates_res(username, base, name, rate) VALUES ('Bent2830', 'Virum', 'VRES-Bellini', 5);

INSERT INTO public.cus_rates_cour(username, courier_id, rate) VALUES ('Frederik2730', 'VCOU-10', 5);
INSERT INTO public.cus_rates_cour(username, courier_id, rate) VALUES ('Aage2730', 'VCOU-10', 9);
INSERT INTO public.cus_rates_cour(username, courier_id, rate) VALUES ('Patrick2830', 'VCOU-4', -10);
INSERT INTO public.cus_rates_cour(username, courier_id, rate) VALUES ('Bent2830', 'VCOU-4', 0);
