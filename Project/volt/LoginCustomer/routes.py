#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from volt.voltForms import CustomerLoginForm
from flask_login import login_user, current_user, logout_user, login_required
from volt.modelsVolt import Customers, select_Customers


Login = Blueprint('Login', __name__)

posts = [{}]


@Login.route("/")
@Login.route("/homepage")
def homepage():
    return render_template('homepage.html', posts=posts)


@Login.route("/customerLogin", methods=['GET', 'POST'])
def customerLogin():
    if current_user.is_authenticated: # redirects to customer homepage if user is logged in
        return redirect(url_for('cusHomepage.customerHomepage'))

    form = CustomerLoginForm() 
    if form.validate_on_submit(): # if not logged in
        user = select_Customers(form.id.data)
        if user != None and user[1] == form.password.data:
            session['base'] = user[0] # saves base to session
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('cusHomepage.customerHomepage'))
    return render_template('customerLogin.html', title='Login', form=form)


@Login.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('Login.homepage'))