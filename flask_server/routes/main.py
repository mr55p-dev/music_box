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
    userBoxes = Box.query.filter_by(userID=current_user.id).all()
    return render_template('profile.html', 
        name = current_user.name,
        boxes = userBoxes
    )

@main.route('/register', methods=["POST"])
@login_required
def registerBox():
    boxName = request.form.get("boxName")
    boxToken = request.form.get("boxToken")

    if Box.query.filter_by(boxToken=boxToken).first():
        flash("This box token is already registered.")
        return redirect(url_for('main.register'))
    
    newBox = Box(
        boxName = boxName,
        boxToken = boxToken,
        userID = current_user.id
    )
    db.session.add(newBox)
    db.session.commit()
    flash("Your box has been added.")
    return redirect(url_for('main.profile'))

@main.route('/box/<boxID>')
@login_required
def boxView(boxID):
    # Validate if the current user is the registered user of the box
    # if current_user.id not in [i.userID for i in Box.query.filter_by(boxID=boxID).all()]:
    #     flash("This box is not registered to you, please check the link and try again.")
    #     return redirect(url_for('main.profile'))

    current_box = Box.query.filter_by(boxID=boxID).first()
    if current_box.userID is not current_user.id:
        flash("This box is not registered to you, please check the link and try again.")
        return redirect(url_for('main.profile'))
    
    return render_template('boxes.html', box = current_box)
    