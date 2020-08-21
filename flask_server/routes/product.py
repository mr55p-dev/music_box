from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
from flask_login import login_required
from flask_server import db
from flask_server.database.models import Song
from flask_server.pool.assign import add_to_queue
from werkzeug.utils import secure_filename
import os
import logging


product = Blueprint('product', __name__)
product_log = logging.getLogger('product_log')


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.')[-1].lower() in current_app.config["ALLOWED_FILETYPES"]


@product.route('/upload', methods=["POST"])
@login_required
def save_song():
    """
    Function to allow a user to upload their own music and
    make it available in the application.
    Currently the filetypes allowed are stored in

        `app.config["ALLOWED_FILETYPES"]`

    These will only be those supported by ffplay
    in the current version of the program.
    """

    # Get the form arguments and file from the request object
    song_name = request.form.get('songName')
    song_artist = request.form.get('songArtist')
    song_description = request.form.get('songDescription')
    song_file = request.files["songFile"]

    # Validate if the file has been uploaded sucessfully and
    # the filetype is valid.
    if song_file.filename == '':
        product_log.info("Song filename None")
        flash("Please upload a song.")
        return redirect(url_for('product.upload_song'))

    # Secure filename removes any '../../' globs from the filename
    song_filename = secure_filename(song_file.filename)
    if not allowed_file(song_filename):
        product_log.info("Invalid file type")
        flash("Invalid filetype.")
        return redirect(url_for('product.upload_song'))

    # Define the upload folder and save the file
    song_dir = current_app.config['UPLOAD_FOLDER']
    song_path = os.path.join(song_dir, song_filename)
    song_file.save(song_path)

    # Create a new database object with the relevant information
    new_song = Song(
        name=song_name,
        artist=song_artist,
        description=song_description,
        path=song_path
    )

    # Commit to the database
    db.session.add(new_song)
    db.session.commit()

    flash("Upload succesfull.")
    return redirect(url_for('product.show_songs'))


@product.route('/upload', methods=['GET'])
@login_required
def upload_song():
    return render_template('upload.html')


@product.route('/songs', methods=["GET"])
def show_songs():
    songs = [i for i in Song.query.all()]
    return render_template('songs.html', songs=songs)


@product.route('/play')
def play_song():
    song_id = request.args.get("id")
    song = Song.query.filter_by(id=song_id).first()
    if not song_id or not song:
        return "Resource not found", 404

    product_log.info(f"Attempting to queue: {song.path}")
    add_to_queue(song.path)

    return "Playing?"
