#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint
from volt import app, conn, bcrypt
from flask_login import current_user
from volt.modelsVolt import selectCourierOrders, selectTakeoutOrders
import sys, datetime

Customer = Blueprint('Customer', __name__)

@Customer.route("/myorders", methods=['GET', 'POST'])
def myorders():
    if not current_user.is_authenticated:
        return redirect(url_for('Login.customerLogin'))
    orders1 = selectCourierOrders(current_user.get_id())
    orders2 = selectTakeoutOrders(current_user.get_id())
    return render_template('customerOrders.html', title='Orders', inv_cd_list1=orders1, inv_cd_list2=orders2)
