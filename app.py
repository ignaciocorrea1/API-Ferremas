from flask import Flask
from api.routes.routes import register_routes
from api.database.database import init_db

# Instancia de Flask
app = Flask(__name__)

# Configuración MySQL
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ferremas"

# Inicialización de MySQL
mysql = init_db(app)

# Registro de rutas
register_routes(app, mysql)

# Inicializacion del servidor solo desde este archivo
if __name__ == "__main__":
    app.run(debug=True)