#from flask import Blueprint, render_template, request

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .model import Buyer
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home(): 
    return render_template('webcart.html')