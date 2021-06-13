#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from volt.voltForms import RestaurantLoginForm
from flask_login import current_user 
from volt.modelsVolt import receivedTakeOrders, receivedCouOrders, receivedRates
import sys, datetime


Restaurant = Blueprint('Restaurant', __name__)


@Restaurant.route("/receivedorders", methods=['GET', 'POST'])
def receivedorders():
    pw = session.get('pw', None)
    if not current_user.is_authenticated:
        return redirect(url_for('rLogin.restaurantLogin'))
    takeOutorders = receivedTakeOrders(pw, current_user.get_id())
    courierOrders = receivedCouOrders(pw, current_user.get_id())
    rates = receivedRates(pw, current_user.get_id())
    return render_template('restaurantOrders.html', title='Orders', inv_cd_list=takeOutorders, inv_cd_list2=rates, inv_cd_list3=courierOrders)
