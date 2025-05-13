from flask import Blueprint, jsonify, request
from api.services.producto_service import ProductoService
from api.services.dolar_service import DolarService

def register_routes(app, mysql):
    """ Blueprints """
    productos = Blueprint("productos", __name__)
    externalAPIs = Blueprint("externalAPIs", __name__)
    
    """ Servicios """
    producto_service = ProductoService(mysql)
    dolar_service = DolarService()
    
    """ Rutas """
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
    
    # GET valor del dolar 
    @externalAPIs.route("/valorDolar/", methods=["GET"])
    def get_valor_dolar():
        valor = dolar_service.get_dolar_today()
        return jsonify(valor)
    
    # PUT precios a USD
    @productos.route("/actualizarUSD/", methods=["PUT"])
    def actualizar_usd():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"estado": "Error", "mensaje": "No se proporcionó data"}), 400
                
            valor = data.get('valor')
            if valor is None:
                return jsonify({"estado": "Error", "mensaje": "Campo 'valor' faltante"}), 400
                
            print(f"Recibido valor para actualización: {valor}")
                
            success = producto_service.put_precio_usd(float(valor))
            return jsonify({"estado": "Éxito", "mensaje": "Precios actualizados"}), 200
                        
        except Exception as e:
            print(f"Error en actualizar_usd: {str(e)}")
            return jsonify({"estado": "Error", "mensaje": str(e)}), 500
    
    # PUT precios a CLP
    @productos.route("/actualizarCLP/", methods=["PUT"])
    def actualizar_clp():
        try:
            data = request.get_json()
            if not data:
                return jsonify({"estado": "Error", "mensaje": "No se proporcionó data"}), 400
                
            valor = data.get('valor')
            if valor is None:
                return jsonify({"estado": "Error", "mensaje": "Campo 'valor' faltante"}), 400
                
            print(f"Recibido valor para actualización: {valor}")
                
            success = producto_service.put_precio_clp(float(valor))
            return jsonify({"estado": "Éxito", "mensaje": "Precios actualizados"}), 200
                        
        except Exception as e:
            print(f"Error en actualizar_clp: {str(e)}")
            return jsonify({"estado": "Error", "mensaje": str(e)}), 500
    
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
    app.register_blueprint(externalAPIs)