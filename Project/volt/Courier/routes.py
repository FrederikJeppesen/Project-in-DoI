#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from flask_login import current_user 
from volt.modelsVolt import receivedOrdersC, receivedRatesC
import sys, datetime


Courier = Blueprint('Courier', __name__)


@Courier.route("/receivedordersC", methods=['GET', 'POST'])
def receivedordersC():
    pw = session.get('pw', None)
    if not current_user.is_authenticated:
        return redirect(url_for('cLogin.courierLogin'))
    orders = receivedOrdersC(pw, current_user.get_id())
    rates = receivedRatesC(current_user.get_id())
    return render_template('courierOrders.html', title='Orders', inv_cd_list=orders, inv_cd_list2 = rates)