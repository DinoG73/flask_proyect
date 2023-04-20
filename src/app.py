from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
import time
from datetime import datetime


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)

#from app import routes
@app.route('/')
# def hello_world():
#      return "<p>Hello, World!</p>"

def index():
    conn = mysql.connect()
    cursor = conn.cursor()

    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)

    empleado = cursor.fetchall()

    #print(empleado)

    conn.commit()

    return render_template('empleados/index.html', empleados=empleado)

@app.route('/create')
def create():
    return render_template('empleados/create.html')


@app.route('/store', methods=["POST"])
def store():
    _nombre = request.form['txt_name']
    _correo = request.form['txt_email']
    _foto = request.files['txt_picture']

    sql = "INSERT INTO empleados (nombre, correo, foto) values (%s, %s, %s);"
    datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


