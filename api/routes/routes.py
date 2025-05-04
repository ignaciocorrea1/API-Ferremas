from flask import Blueprint, jsonify

"""
    Blueprint: se usa para organizar y agrupar rutas que se relacionan entre si.
"""

def register_routes(app, mysql):
    productos = Blueprint("productos", __name__)
    
    @productos.route("/productos", methods=["GET"])
    def get_productos():
        try:
            cur = mysql.connection.cursor()
            cur.execute("SELECT * FROM productos")  
            productos = cur.fetchall()
            cur.close()
            return jsonify({"estado": "ok", "productos": productos})
        except Exception as e:
            return jsonify({"estado": "error", "mensaje": str(e)}), 500
    
    
    """ Validar la conexion con la BD """
    @app.route("/validar", methods=["GET"])
    def validacion():
        try:
            # Se establece una conexión con la BD
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            resultado = cur.fetchone() # Obtención de la primera fila solo
            cur.close()
            return jsonify({"estado": "conectado", "mensaje": resultado})
        except Exception as e:
            return jsonify({"estado": "error", "mensaje": str(e)}), 500
        
    app.register_blueprint(productos)