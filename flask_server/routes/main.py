from flask import Blueprint, render_template, flash, request, url_for, redirect
from flask_login import current_user, login_required
from flask_server.database.models import User 
from flask_server import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')
