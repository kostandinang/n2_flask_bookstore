from flask import render_template, Blueprint, abort, request, redirect, url_for
from app import db
db = db.db_instance
home = Blueprint("home", __name__)

@home.route('/')
def index():
    try:
        # Query
        cur = db.connection.cursor()
        query = ''' SELECT id, title, cover FROM book ORDER BY year LIMIT 8'''
        cur.execute(query)
        rows = cur.fetchall();
        books = []
        for row in rows:
            books.append({
                'id': row[0],
                'title': row[1],
                'cover': row[2]
                })
        return render_template('index.html', books=books)
    except Exception as e:
        abort(500, e)
    return render_template('index.html')
