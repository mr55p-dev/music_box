from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_server.database.models import User
from flask_server import db
import logging

auth = Blueprint('auth', __name__)
auth_log = logging.getLogger('auth_log')


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=["POST"])
def login_post():
    email = request.form.get('email').lower()
    password = request.form.get('password')
    remember = True if request.form.get('checkbox') else False

    user = User.query.filter_by(email=email).first()
    if not user:
        auth_log.info("Invalid email")
        flash("Your email is incorrect.")
        return redirect(url_for('auth.login'))

    if not check_password_hash(user.password, password):
        auth_log.info("Invalid password")
        flash("Your password is incorrect.")
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    auth.log(f"logged in user: {user.name}")
    return redirect(url_for('main.index'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=["POST"])
def signup_post():
    name = request.form.get("name")
    email = request.form.get("email").lower()
    password = request.form.get("password")

    if User.query.filter_by(email=email).first():

        flash("This email is already associated with an account.")
        return redirect(url_for('auth.signup'))

    new_user = User(
        email=email,
        name=name,
        password=generate_password_hash(password)
    )

    db.session.add(new_user)
    db.session.commit()
    auth_log.info(f"Created new user: {new_user.name}")

    new_user = User.query.filter_by(email=new_user.email).first()
    login_user(new_user)
    auth_log.info(f"Logged in user: {new_user.name}")
    return redirect(url_for('main.index'))


@auth.route('/logout')
@login_required
def logout():
    auth_log.info(f"Logged out user: {current_user.name}")
    logout_user()
    return redirect(url_for('main.index'))
