from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL
import time
from datetime import datetime
import os

#Flask app
app = Flask(__name__)
#SQL object
mysql = MySQL()
#DB connection
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'empleados'

UPLOADS = os.path.join('uploads')
app.config['UPLOADS'] = UPLOADS

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

    return render_template('empleados/index.html', empleado=empleado)


@app.route('/create')
def create():
    return render_template('empleados/create.html')


@app.route('/store', methods=['POST'])
def store():
    _nombre = request.form['txt_name']
    _correo = request.form['txt_email']
    _foto = request.files['txt_picture']

    now = datetime.now()
    print(now)
    timee = now.strftime("%Y%H%M%S")
    print(timee)

    if _foto.filename != '':
        new_name_pic = timee + '_' + _foto.filename # Esta linea marca un error o advertencia en vs code, todavia no deduzco de que se trata
        _foto.save("src/uploads/" + new_name_pic)


    sql = "INSERT INTO empleados (nombre, correo, foto) values (%s, %s, %s);"
    datos = (_nombre, _correo, _foto.filename)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()

    return redirect('/')


@app.route('/delete/<int:id>')
def delete(id):
    print('hola')
    sql = "DELETE FROM  empleados WHERE id=%s"
    # sql = f'DELETE FROM  empleados WHERE id={id}'
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql, id)
    # cursor.execute(sql)
    conn.commit()

    return redirect('/')


@app.route('/modify/<int:id>')
def modify(id):
    print(id)
    sql = f"SELECT * FROM empleados WHERE id={id}"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    empleado = cursor.fetchone()
    conn.commit()
    return render_template('empleados/edit.html', empleado=empleado)


@app.route('/update', methods=['POST'])
def update():
    _nombre = request.form['txt_name']
    _correo = request.form['txt_email']
    _foto = request.files['txt_picture']
    id = request.form['txt_id']

    datos = (_nombre, _correo, id)

    conn = mysql.connect()
    cursor = conn.cursor()

   

    if _foto.filename != '':
        now = datetime.now()
        timee = now.strftime("%Y%H%M%S")
        new_name_pic = timee + '_' + _foto.filename # Esta linea marca un error o advertencia en vs code, todavia no deduzco de que se trata
        _foto.save("src/uploads/" + new_name_pic)


    sql = f'SELECT foto FROM empleados WHERE id={id}'
    cursor.execute(sql)

    nombre_foto = cursor.fetchone()[0]

    os.remove(os.path.join(app.config['UPLOADS'], nombre_foto))

    #datos = (_nombre, _correo, _foto.filename)

    # conn = mysql.connect()
    # cursor = conn.cursor()

    sql = f'UPDATE empleados SET nombre={_nombre}, correo={_correo} WHERE id={id}'
    cursor.execute(sql)
    conn.commit()





if __name__ == '__main__':
    app.run(debug=True)


