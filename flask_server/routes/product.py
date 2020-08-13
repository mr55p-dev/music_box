from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from flask_server.database.models import User, Box
from flask_server import db

product = Blueprint('product', __name__)

@product.route('/register', methods=["POST"])
@login_required
def registerBox():
    boxName = request.form.get("boxName")
    boxToken = request.form.get("boxToken")

    if Box.query.filter_by(boxToken=boxToken).first():
        flash("This box token is already registered.")
        return redirect(url_for('product.register'))
    
    newBox = Box(
        boxName = boxName,
        boxToken = boxToken,
        userID = current_user.id
    )
    db.session.add(newBox)
    db.session.commit()
    flash("Your box has been added.")
    return redirect(url_for('main.profile'))


@product.route('/box/<boxID>')
@login_required
def boxView(boxID):
    # Validate if the current user is the registered user of the box
    current_box = Box.query.filter_by(boxID=boxID).first()
    if current_box.userID is not current_user.id:
        flash("This box is not registered to you, please check the link and try again.")
        return redirect(url_for('main.profile'))
    
    return render_template('boxes.html', box = current_box)