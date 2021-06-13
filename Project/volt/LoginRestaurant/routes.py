#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from volt.voltForms import RestaurantLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from volt.modelsVolt import Restaurants, select_Restaurants


rLogin = Blueprint('rLogin', __name__)

posts = [{}]


@rLogin.route("/")
@rLogin.route("/homepage")
def homepage():
    return render_template('homepage.html', posts=posts)


@rLogin.route("/restaurantLogin", methods=['GET', 'POST'])
def restaurantLogin():
    if current_user.is_authenticated: # redirects to restaurant homepage if user is logged in
        return redirect(url_for('Restaurant.receivedorders'))
    
    form = RestaurantLoginForm()
    if form.validate_on_submit(): # if not logged in
        user = select_Restaurants(form.password.data, form.id.data)
        if user != None and user[0] == form.password.data:
            session['pw'] = user[0] # saves password to session
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('Restaurant.receivedorders'))
    return render_template('restaurantLogin.html', title='Login', form=form)


@rLogin.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('rLogin.homepage'))