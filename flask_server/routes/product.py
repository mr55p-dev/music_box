from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import current_user, login_required
from flask_server import db
from flask_server.database.models import User, Box, Song
from flask_server.utils.decorators import requiresOwnership, trace

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
    # Big problem with this line here, some work needed on querying the relation - figure it out !!!
    current_box = Box.owner.has(User.id==current_user.id)
    return render_template('boxes.html', box = current_box)

@product.route('/box/<boxID>/addSong', methods=["POST"])
@login_required
def addSongToBox(boxID):
    """
    This is a tempoary method which is just meant to test
    accessing one property through another in the database
    models. Needs to be replaced with something that also 
    communicates with the box and writes the song / checks
    which songs are on the box.
    """
    return "AddSong"

@product.route('/box/<boxID>/addSong')
@login_required
def boxSongsPage(boxID):
    """
    Again a tempoary method which just allows viewing the
    songs in the database, it doesnt work properly as 
    there are no boxes in real life and no clients to communicate
    with. Just for testing.
    """
    all_songs = Song.query.all()
    box_songs = Box.query.filter_by(boxID=boxID).first().songs
    current_box = Box.query.filter_by(boxID=boxID).first()

    return render_template('song-add.html', 
        all_songs = all_songs,
        box_songs = box_songs,
        box = current_box
    )
