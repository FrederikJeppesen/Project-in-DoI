#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import Flask
import psycopg2
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fc089b9218301ad987914c53481bff04'

db = "dbname='volt' user='postgres' host='localhost' port='5420' password = 'postgres'"
conn = psycopg2.connect(db)

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from volt.LoginCustomer.routes import Login
from volt.Customer.routes import Customer
from volt.LoginRestaurant.routes import rLogin
from volt.Restaurant.routes import Restaurant
from volt.LoginCourier.routes import cLogin
from volt.Courier.routes import Courier
from volt.AddCustomer.routes import cusAdd
from volt.CustomerHomepage.routes import cusHomepage

app.register_blueprint(Login)
app.register_blueprint(rLogin)
app.register_blueprint(cLogin)
app.register_blueprint(Customer)
app.register_blueprint(Restaurant)
app.register_blueprint(Courier)
app.register_blueprint(cusAdd)
app.register_blueprint(cusHomepage)
