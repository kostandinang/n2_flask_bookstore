from flask import render_template, Blueprint, abort, request, redirect, url_for
from app import db
db = db.db_instance
books = Blueprint("books", __name__)

@books.route('/')
def list():
    '''
    Lists books on GET
    Create books on POST
    '''
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

@books.route('/add', methods = ['GET', 'POST'])
def add():
    '''
    Render the create form
    '''
    authors = []
    publishers = []
    book = None
    error = None
    method = request.method

    try:
        if method == 'GET':
            # Authors Query
            cur = db.connection.cursor()
            query = ''' SELECT id, name FROM author '''
            cur.execute(query)
            rows = cur.fetchall();
            for row in rows:
                authors.append({
                    'id': row[0],
                    'name': row[1],
                    })
            
            # Publishers Query
            cur = db.connection.cursor()
            query = ''' SELECT id, name FROM publisher '''
            cur.execute(query)
            rows = cur.fetchall();
            for row in rows:
                publishers.append({
                    'id': row[0],
                    'name': row[1],
                    })
        
        if method == 'POST':    
            #Params
            title = request.form.get('title')
            isbn = request.form.get('isbn')
            year = request.form.get('year')
            cover = request.form.get('cover')
            author = request.form.get('author')
            publisher = request.form.get('publisher')

            if not title or not isbn or not year or not cover or not author or not publisher:
                error = 'Invalid parameters, double check values in the form'
            else:
                 # Query
                cur = db.connection.cursor()
                query = ''' INSERT INTO book (title, isbn, year, cover, author, publisher) VALUES (%s, %s, %s, %s, %s, %s)'''
                cur.execute(query, [title, isbn, year, cover, author, publisher])
                db.connection.commit()
                return redirect(url_for('books.list'))
    except Exception as e:
        db.connection.rollback()
        abort(500, e)
    return render_template('book/book_form.html', book=book, authors=authors, publishers=publishers, error=error)

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