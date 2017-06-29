from flask import render_template, Blueprint, abort, request, redirect, url_for
from app import db

db = db.db_instance
authors = Blueprint("authors", __name__)

@authors.route('/')
def list():
    '''
    Lists authors
    '''
    try:
        authors = []
        return render_template('author/author_index.html', authors=authors)
    except Exception as e:
        abort(500, e)
