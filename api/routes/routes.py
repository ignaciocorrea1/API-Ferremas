from flask import Blueprint, jsonify
from api.services.producto_service import ProductoService

def register_routes(app, mysql):
    """Blueprints"""
    productos = Blueprint("productos", __name__)
    
    """Servicios"""
    producto_service = ProductoService(mysql)
    
    """Rutas"""
    # GET productos
    @productos.route("/productos/", methods=["GET"])
    def get_productos():
        try:
            productos = producto_service.get_productos()
            
            if not productos:
                return jsonify({"estado": "Sin resultados", "Mensaje": "No se encontraron productos"}), 404
            
            return jsonify(productos), 200 
        except Exception as e:
            return jsonify({"Estado": "Error al obtener los productos", "Mensaje": str(e)}), 500
    
    # GET producto por id
    @productos.route("/productos/<int:id>", methods=["GET"])
    def get_producto_by_id(id):
        try:
            producto = producto_service.get_producto_by_id(id)

            if not producto:
                return jsonify({"Estado": "Sin resultados", "Mensaje": "No se encontro producto"}), 404
            return jsonify(producto), 200
        except Exception as e:
            return jsonify({"Estado": "Error al obtener el producto", "Mensaje": str(e)}), 500
    
    # Validar conexion con BD
    @app.route("/validar", methods=["GET"])
    def validacion():
        try:
            # Se establece una conexión con la BD
            cur = mysql.connection.cursor()
            cur.execute("SELECT 1")
            resultado = cur.fetchone() 
            cur.close()
            return {"Estado": "Conectado correctamente con la BD", "Mensaje": resultado}
        except Exception as e:
            return {"Estado": "Error al conectar con la BD", "Mensaje": str(e)}, 500
    
    """ Registro de Blueprints """    
    app.register_blueprint(productos)