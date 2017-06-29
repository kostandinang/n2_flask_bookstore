from flask import render_template, Blueprint, abort, request, redirect, url_for
from app import db

db = db.db_instance
publishers = Blueprint("publishers", __name__)

@publishers.route('/')
def list():
    '''
    Lists publishers
    '''
    try:
        publishers = []
        return render_template('publisher/publisher_index.html', publishers=publishers)
    except Exception as e:
        abort(500, e)
