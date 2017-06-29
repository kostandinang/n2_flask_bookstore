from flask import Flask, render_template

import logging
from logging import Formatter, FileHandler

# ---------------------------------------------------------------------- #
# Init
# ---------------------------------------------------------------------- #

app = Flask(
    '__name__',
    static_url_path='/static',
    static_folder='/home/kostandinang/n2_flask_bookstore/app/static/',
    template_folder='/home/kostandinang/n2_flask_bookstore/app/templates/'
)
app.config.from_object('app.config')

# ---------------------------------------------------------------------- #
# Blueprints
# ---------------------------------------------------------------------- #

from app.views.books import books
from app.views.authors import authors
from app.views.publishers import publishers
app.register_blueprint(books, url_prefix='/books')
app.register_blueprint(authors, url_prefix='/authors')
app.register_blueprint(publishers, url_prefix='/publishers')

# ---------------------------------------------------------------------- #
# Default route
# ---------------------------------------------------------------------- #

@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------------------------------------------------- #
# Errors
# ---------------------------------------------------------------------- #

@app.errorhandler(404)
def not_found_err(error):
    return render_template('errors/404.html', err = error), 404

@app.errorhandler(500)
def not_found_err(error):
    return render_template('errors/500.html', err = error), 500

# ---------------------------------------------------------------------- #
# Logging
# ---------------------------------------------------------------------- #

if not app.debug:
    file_handler = FileHandler('logs/error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')
