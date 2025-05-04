from flask_mysqldb import MySQL

# Instancia de mysql
mysql = MySQL()

# Configura la conexión con la bd, utilizando los parametros de app.py y devuelve
# un objeto tipo mysql para interactuar con la bd
def init_db(app): 
    mysql.init_app(app)
    return mysql