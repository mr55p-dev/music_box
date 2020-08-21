from flask import Blueprint, render_template, flash, request, redirect, url_for, current_app
# from flask_login import login_required
from flask_server import db
from flask_server.database.models import Song
from flask_server.pool.assign import add_to_queue
from werkzeug.utils import secure_filename
import os
import logging


product = Blueprint('product', __name__)
product_log = logging.getLogger('product_log')


@product.route('/upload', methods=["POST"])
# @login_required
def save_song():
    """
    Bla Bla Bla
    """
    song_name = request.form.get('songName')
    song_artist = request.form.get('songArtist')
    song_description = request.form.get('songDescription')
    song_file = request.files["songFile"]

    if song_file.filename == '':
        flash("Please upload a song.")
        return redirect(url_for('product.upload_song'))

    song_filename = secure_filename(song_file.filename)
    song_dir = current_app.config['UPLOAD_FOLDER']
    song_path = os.path.join(song_dir, song_filename)
    song_file.save(song_path)

    new_song = Song(
        name=song_name,
        artist=song_artist,
        description=song_description,
        path=song_path
    )

    db.session.add(new_song)
    db.session.commit()

    flash("Upload succesfull.")
    return redirect(url_for('product.show_songs'))


@product.route('/upload', methods=['GET'])
# @login_required()
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
