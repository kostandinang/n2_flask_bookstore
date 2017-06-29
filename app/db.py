from . import app
from flask_mysqldb import MySQL

db_instance = MySQL(app)
