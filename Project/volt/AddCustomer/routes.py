#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from volt.voltForms import AddCustomerForm
from flask_login import login_user, current_user, logout_user, login_required
from volt.modelsVolt import insert_Customers


cusAdd = Blueprint('cusAdd', __name__)

posts = [{}]

@cusAdd.route("/customerAdd", methods=['GET', 'POST'])
def customerAdd():
    form = AddCustomerForm()
    if form.validate_on_submit():
        insert_Customers(form.base.data, form.password.data, form.username.data, form.zone.data)
        return redirect(url_for('Login.customerLogin'))
    return render_template('customerAdd.html', title='Login', form=form)
