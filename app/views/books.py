from flask import render_template, Blueprint, abort, request, redirect, url_for
from app import db
db = db.db_instance
books = Blueprint("books", __name__)

@books.route('/', methods=['GET', 'POST'])
def list():
    '''
    Lists books on GET
    Create books on POST
    '''
    method = request.method
    
    if method == 'GET':
        try:
            # Params
            title = request.args.get('title') or None
            # Query
            cur = db.connection.cursor()
            query = ''' SELECT * FROM book WHERE (%s IS NULL OR title = %s)'''
            cur.execute(query, [title, title])
            rows = cur.fetchall();
            books = []
            for row in rows:
                books.append({
                    'id': row[0],
                    'title': row[1],
                    'isbn': row[2],
                    'year': row[3],
                    'cover': row[4]
                    })
            return render_template('book/book_index.html', books=books)
        except Exception as e:
            abort(500, e)

@books.route('/add')
def add():
    '''
    Render the create form
    '''
    book = None
    return render_template('book/book_form.html', book=book)

@books.route('/<id>', methods=['GET', 'PUT', 'DELETE'])
def actions(id=None):
    '''
    Performs actions on a record with id
    Get details on GET
    Update on PUT
    Delete on DELETE
    '''
    method = request.method

    if method == 'DELETE':
        if id:
            # Query
            cur = db.connection.cursor()
            query = ''' DELETE FROM book WHERE ID = %s''' % id
            cur.execute(query)
            db.connection.commit()
            return "success"
        else:
            abort(500, 'No id is provided')

    elif method == 'GET':
        try:
            # Query
            cur = db.connection.cursor()
            query = ''' SELECT book.id, book.title, book.isbn, book.year, book.cover, book.author, author.name, book.publisher, publisher.name FROM book 
            INNER JOIN author ON book.author = author.id 
            INNER JOIN publisher ON publisher = publisher.id 
            WHERE (book.id = %s)''' % id
            cur.execute(query)
            row = cur.fetchone();
            book = None
            if row:
                book = {
                    'id': row[0],
                    'title': row[1],
                    'isbn': row[2],
                    'year': row[3],
                    'cover': row[4],
                    'author': {
                        'id': row[5],
                        'name': row[6]
                    },
                    'publisher': {
                        'id': row[7],
                        'name': row[8]
                    }
                }
            return render_template('book/book_detail.html', book=book)
        except Exception as e:
            abort(500, e)