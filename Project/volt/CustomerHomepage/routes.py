#Patrick Jensen (mxf667) & Frederik Jeppesen (wcn773)
from flask import render_template, url_for, flash, redirect, request, Blueprint, session
from volt import app, conn, bcrypt
from flask_login import current_user
from volt.voltForms import AddFoodForm
from volt.modelsVolt import activeOrderNums, listOfmeals, insert_Foodorders, insert_Receives, insert_CourOrders, insert_TakeOut
import datetime as dt
import random as rd


cusHomepage = Blueprint('cusHomepage', __name__)


@cusHomepage.route("/customerHomepage", methods=['GET', 'POST'])
def customerHomepage():
    form = AddFoodForm()
    base = session.get('base', None)
    
    if not current_user.is_authenticated:
        return redirect(url_for('Login.customerLogin'))

    foodList = listOfmeals(base) # list of tuples, we want to format it so that we dynamically have process the right types and at the same time show a properly formatted string on the page.
    for i in range(len(foodList)):
        foodList[i] = list(foodList[i]) # makes tuples to list
    
    strFoodList = []
    for fl in foodList:
        strFoodList.append([str(i) for i in fl]) # makes all elements in inner lists string type to properly split later
    
    finalstrFoodList = [' '.join(i) for i in strFoodList] # makers the list of lists to a list of strings
    showstrFoodList = [i.replace('_', ' ') for i in finalstrFoodList] # replaces underscore in two-word food names

    actualChoiceList = []
    for i in range(len(finalstrFoodList)):
        actualChoiceList.append((finalstrFoodList[i], showstrFoodList[i])) # combines the two lists to pass to our radiobutton form

    form.choice.choices = actualChoiceList # passing tuple of the two formatted lists, element by element as a list of tuples 
    checkTakeout = form.takeout.data # selected choice

    if form.choice.data != None: 
        FC = form.choice.data.split(' ') # receives a string that can be split up to get data values
        if FC[0] == 'Herlev':
            courierId = 'VCOU-10'
        else:
            courierId = 'VCOU-4'

        orderNr = len(activeOrderNums()) # ordernumber is highest active order number + 1
        
        insert_Foodorders(orderNr, str(dt.datetime.today().replace(microsecond=0)), FC[2], float(FC[3]), 1, current_user.get_id())
        insert_Receives(orderNr, FC[1], FC[0], courierId)
        
        if checkTakeout == True:
            insert_TakeOut(orderNr, str((dt.datetime.today()+dt.timedelta(minutes=30)).replace(microsecond=0)))
            return redirect(url_for('Customer.myorders'))
        else:
            insert_CourOrders(orderNr, str((dt.datetime.today()+dt.timedelta(minutes=30)).replace(microsecond=0)))
            return redirect(url_for('Customer.myorders'))

    return render_template('customerHomepage.html', form=form, title='Login')
