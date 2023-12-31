from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .model import Buyer
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')

        buyer = Buyer.query.filter_by(Phone_number = phone_number).first()

        if buyer:
            if buyer.password == password:
                #login_user(buyer, remember=True)
                print('successfully logged in')
                return redirect(url_for('auth.login'))
            else:
                return redirect(url_for('auth.login'))
        else:
            return redirect(url_for('auth.login'))
        
    return render_template("login.html")
       
