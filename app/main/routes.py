from . import main

from flask import render_template, redirect,url_for, current_app

@main.route('/')
def index():
    now_playing = current_app.movieapi.get_now_playing()

    context = {
        'now_playing': now_playing[0:5]
    }
    return render_template('index.html', **context)
