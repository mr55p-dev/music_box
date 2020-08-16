from flask import Blueprint, render_template, flash, request, url_for, redirect
from flask_login import current_user, login_required
from flask_server.database.models import User, Box
from flask_server import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
    
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', 
        name = current_user.user_name,
        boxes = current_user.user_boxes
    )

    