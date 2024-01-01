from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, logout_user, current_user
from .model import Buyer
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        password = request.form.get('password')
        buyer = Buyer.query.filter_by(Phone_number=phone_number).first()
        
        if buyer and buyer.Password == password:
            # login_user(buyer, remember=True)  # Uncomment this if you're using Flask-Login
            session['user_name'] = f"{buyer.First_Name} {buyer.Last_Name}" 
            return redirect(url_for('views.home'))
        else:
            # Handle login failure
            return redirect(url_for('auth.login'))

    return render_template("login.html")
       
@auth.route('/logout')
def logout():
    # logout_user()  # Uncomment this if you're using Flask-Login
    session.pop('user_id', None)  # Remove user information from session
    session.pop('user_name', None)
    return redirect(url_for('views.home'))