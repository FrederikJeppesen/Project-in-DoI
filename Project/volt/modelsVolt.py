#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from datetime import datetime
from volt import conn, login_manager
from flask_login import UserMixin
from psycopg2 import sql


@login_manager.user_loader
def load_user(username):
    cur = conn.cursor()

    schema = 'customers'
    id = 'username'

    if str(username).startswith('VRES-'):
        schema = 'restaurants'
        id = 'name'
    elif str(username).startswith('VCOU-'):
        schema = 'couriers'
        id = 'courier_id'

    user_sql = sql.SQL("""
    SELECT * FROM {}
    WHERE {} = %s
    """).format(sql.Identifier(schema),  sql.Identifier(id))

    print("SCHEMA =", schema)
    
    cur.execute(user_sql, (str(username),))
    if cur.rowcount > 0:
        return Customers(cur.fetchone()) if schema == 'customers' else (Restaurants(cur.fetchone()) if schema == 'restaurants' else (Couriers(cur.fetchone())))
    else:
        return None


class Customers(tuple, UserMixin):
    def __init__(self, user_data):
        self.base = user_data[0]
        self.password = user_data[1]
        self.username = user_data[2]
        self.zone = user_data[3]

    def get_id(self):
       return (self.username)

class Restaurants(tuple, UserMixin):
    def __init__(self, employee_data):
        self.base = employee_data[0]
        self.name = employee_data[1]
        self.zone = employee_data[2]

    def get_id(self):
       return (self.name)

class Couriers(tuple, UserMixin):
    def __init__(self, employee_data):
        self.capacity = employee_data[0]
        self.base = employee_data[1]
        self.courier_id = employee_data[2]
        self.zone = employee_data[3]

    def get_id(self):
       return (self.courier_id)


def select_Customers(username):
    cur = conn.cursor()
    sql = """
    SELECT * FROM Customers
    WHERE username = %s
    """
    cur.execute(sql, (username,))
    user = Customers(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user 

def selectCourierOrders(username):
    print(username)
    cur = conn.cursor()
    sql = """
    SELECT F.order_nr, F.time_of_order, F.meal_name, F.price, F.nr_of_dishes, R.name, R.base, C.eta
    FROM food_orders F, receives R, courier_orders C
    WHERE C.order_nr = F.order_nr AND C.order_nr = R.order_nr AND F.order_nr = R.order_nr AND username = %s
    """
    cur.execute(sql, (username,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def selectTakeoutOrders(username):
    print(username)
    cur = conn.cursor()
    sql = """
    SELECT F.order_nr, F.time_of_order, F.meal_name, F.price, F.nr_of_dishes, R.name, R.base, T.pick_up_time
    FROM food_orders F, receives R, take_out_orders T
    WHERE T.order_nr = F.order_nr AND T.order_nr = R.order_nr AND F.order_nr = R.order_nr AND username = %s
    """
    cur.execute(sql, (username,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def select_Restaurants(base, name):
    print("select_Restaurants")
    print("base, name:", base, name)
    cur = conn.cursor()
    sql = """
    SELECT * FROM Restaurants
    WHERE base = %s AND name = %s
    """ #% (base, name,)
    cur.execute(sql, (base, name,))
    user = Restaurants(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def receivedTakeOrders(base, name):
    print("receivedTakeOrders")
    print("base, name:", base, name)
    cur = conn.cursor()
    sql = """
    SELECT F.order_nr, F.time_of_order, F.meal_name, F.price, F.nr_of_dishes, T.pick_up_time, F.username
    FROM food_orders F, receives R, take_out_orders T
    WHERE T.order_nr = F.order_nr AND T.order_nr = R.order_nr AND F.order_nr = R.order_nr AND base = %s AND name = %s
    """
    cur.execute(sql, (base, name))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def receivedCouOrders(base, name):
    print("receivedCouOrders")
    print("base, name:", base, name)
    cur = conn.cursor()
    sql = """
    SELECT F.order_nr, F.time_of_order, F.meal_name, F.price, F.nr_of_dishes, R.courier_id, F.username
    FROM food_orders F, receives R, courier_orders C
    WHERE C.order_nr = F.order_nr AND C.order_nr = R.order_nr AND F.order_nr = R.order_nr AND base = %s AND name = %s
    """
    cur.execute(sql, (base, name))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def select_Couriers(base, courier_id):
    print("select_Couriers")
    print("base, courier_id:", base, courier_id)
    cur = conn.cursor()
    sql = """
    SELECT * FROM Couriers
    WHERE base = %s AND courier_id = %s
    """
    cur.execute(sql, (base, courier_id,))
    user = Couriers(cur.fetchone()) if cur.rowcount > 0 else None;
    cur.close()
    return user

def receivedOrdersC(base, courier_id):
    print("receivedOrdersC")
    print("base, courier_id:", base, courier_id)
    cur = conn.cursor()
    sql = """
    SELECT R.order_nr, R.name, R.base, F.time_of_order, F.username, C.base
    FROM receives R, food_orders F, customers C
    WHERE R.order_nr = F.order_nr AND F.username = C.username AND R.base = C.base AND R.base = %s AND R.courier_id = %s
    """
    cur.execute(sql, (base, courier_id))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def insert_Customers(base, password, username, zone):
    cur = conn.cursor()
    sql = """
    INSERT INTO Customers(base, password, username, zone)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (base, password, username, zone))
    conn.commit()
    cur.close()

def listOfmeals(base):
    print("listOfmeals")
    print("base, name:", base)
    cur = conn.cursor()
    sql = """
    SELECT base, name, meal_name, price 
    FROM makes
    WHERE base = %s
    """
    cur.execute(sql, (base,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def insert_Foodorders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username):
    cur = conn.cursor()
    sql = """
    INSERT INTO Food_orders(order_nr, time_of_order, meal_name, price, nr_of_dishes, username)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cur.execute(sql, (order_nr, time_of_order, meal_name, price, nr_of_dishes, username))
    conn.commit()
    cur.close()

def insert_Receives(order_nr, name, base, courier_id):
    cur = conn.cursor()
    sql = """
    INSERT INTO Receives(order_nr, name, base, courier_id)
    VALUES (%s, %s, %s, %s)
    """
    cur.execute(sql, (order_nr, name, base, courier_id))
    conn.commit()
    cur.close()

def insert_CourOrders(order_nr, eta):
    cur = conn.cursor()
    sql = """
    INSERT INTO Courier_orders(order_nr, eta)
    VALUES (%s, %s)
    """
    cur.execute(sql, (order_nr, eta))
    conn.commit()
    cur.close()

def receivedRates(base, name):
    print("receivedRates")
    print("base, name:", base, name)
    cur = conn.cursor()
    sql = """
    SELECT username, rate
    FROM cus_rates_res
    WHERE base = %s AND name = %s
    """
    cur.execute(sql, (base, name))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def receivedRatesC(courier_id):
    print("receivedRatesC")
    print("courier_id:", courier_id)
    cur = conn.cursor()
    sql = """
    SELECT username, rate
    FROM cus_rates_cour
    WHERE courier_id = %s
    """
    cur.execute(sql, (courier_id,))
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset

def insert_TakeOut(order_nr, pick_up_time):
    cur = conn.cursor()
    sql = """
    INSERT INTO Take_out_orders(order_nr, pick_up_time)
    VALUES (%s, %s)
    """
    cur.execute(sql, (order_nr, pick_up_time))
    conn.commit()
    cur.close()

def activeOrderNums():
    cur = conn.cursor()
    sql = """
    SELECT order_nr
    FROM Food_orders
    """
    cur.execute(sql, ())
    tuple_resultset = cur.fetchall()
    cur.close()
    return tuple_resultset
