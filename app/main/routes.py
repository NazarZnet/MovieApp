from . import main

from flask import render_template, redirect,url_for, current_app

@main.route('/')
def index():
    now_playing = current_app.movieapi.get_now_playing()
    popular= current_app.movieapi.get_popular()
    top_rated = current_app.movieapi.get_top_rated()
    upcoming = current_app.movieapi.get_upcoming()

    context = {
        'now_playing': now_playing[0:5],
        'popular': popular[5:10],
        'top_rated': top_rated[0:5],
        'upcoming': upcoming[5:15]
    }
    return render_template('index.html', **context)
