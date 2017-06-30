# Bookstore
### A minimal flask app

This app is ready to be installed on https://www.pythonanywhere.com environment 

## Installation

- Enter pythonanywhere bash console
- Checkout this repository into your bash using the command
```
git clone https://github.com/kostandinang/n2_flask_bookstore.git
```
- Install libraries
```
pip install --user flask-mysqldb
```
- Go to Web Tab in PythonAnywhere
- In Code section change source code value to /home/**user**/n2_flask_bookstore where **user** is your PythonAnywhere username

- Reload the webapp

## Configuration
After you have successfuly installed the app and its libraries change database configuration to use the connection from PythonAnywhere environment

- Go to web section - code and click on /var/www/kostandinang_pythonanywhere_com_wsgi.py
- Change project_home to:

```
u'/home/user/n2_flask_bookstore'
```
where user is your PythonAnywhere username
- Change the last line to:

```
from server import app as application
```

- Change /home/**user**/n2_flask_bookstore/app/config.py MYSQL_* config values using the values from
https://www.pythonanywhere.com/user/**user**/databases/ (where **user** is your PythonAnywhere username)

```
MYSQL_USER = 'kostandinang'
MYSQL_PASSWORD = 'b00kst0r3'
MYSQL_DB = 'kostandinang$n2_bookstore'
MYSQL_HOST = 'kostandinang.mysql.pythonanywhere-services.com'
```

- Also change the username in in /app/__init.py__ (Requirements for pythonanywhere.com)
Replace **kostandinang** with your pythonanywhere username

```
app = Flask(
    '__name__',
    static_url_path='/static',
    static_folder='/home/kostandinang/n2_flask_bookstore/app/static/',
    template_folder='/home/kostandinang/n2_flask_bookstore/app/templates/'
)
```

## Import Schema & Sample Data
Import database schema and sample data into PythonAnywhere db.
- Copy the file from /data.sql
- Paste the copied content into Mysql shell in PythonAnywhere

## Run the app on 
[http://user.pythonanywhere.com](http://user.pythonanywhere.com) where **user** is your PythonAnywhere username
