from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empleados'

if __name__ == '__main__':
    app.run(debug=True)


# from app import routes
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"