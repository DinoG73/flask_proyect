from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)

#from app import routes
@app.route("/")
# def hello_world():
#      return "<p>Hello, World!</p>"

def index():
    # conn = mysql.connect()
    # cursor = conn.cursor()

    # sql = "insert into empleados (nombre, correo, foto) values ('Bruno', 'bag@gmail.com', 'fotobruno.jpg');"
    # cursor.execute(sql)
    # conn.commit()

    return render_template('empleados/index.html')









if __name__ == '__main__':
    app.run(debug=True)


