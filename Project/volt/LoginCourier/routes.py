#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from volt.voltForms import CourierLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from volt.modelsVolt import Couriers, select_Couriers


cLogin = Blueprint('cLogin', __name__)

posts = [{}]


@cLogin.route("/")
@cLogin.route("/homepage")
def homepage():
    return render_template('homepage.html', posts=posts)


@cLogin.route("/courierLogin", methods=['GET', 'POST'])
def courierLogin():
    if current_user.is_authenticated: # redirects to courier homepage if user is logged in
        return redirect(url_for('Courier.receivedordersC'))
    
    form = CourierLoginForm()
    if form.validate_on_submit(): # if not logged in
        user = select_Couriers(form.password.data, form.id.data)
        if user != None and user[1] == form.password.data:
            session['pw'] = user[1] # saves password to session
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Courier.receivedordersC'))
    return render_template('courierLogin.html', title='Login', form=form)


@cLogin.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('cLogin.homepage'))