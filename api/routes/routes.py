from datetime import datetime
import json
from flask import Blueprint, jsonify, request, redirect
from api.services.pago_service import PagoService
from api.services.producto_service import ProductoService
from api.services.dolar_service import DolarService
from api.services.webpay_service import WebpayService

def register_routes(app, mysql):
    """ Blueprints """
    productos = Blueprint("productos", __name__)
    externalAPIs = Blueprint("externalAPIs", __name__)
    
    """ Servicios """
    pago_service = PagoService(mysql)
    producto_service = ProductoService(mysql)
    dolar_service = DolarService()
    webpay_service = WebpayService()
    
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
    
    """ ------------------------------------------------------------------------------------------------------- """
    # Crear transacción de webpay
    @app.route('/crear_transaccion', methods=["POST"])
    def crear_transaccion():
        data = request.get_json()
        if not data:
            return jsonify({"estado": "Error", "detalle": "JSON no recibido"}), 400

        nro_orden = data.get("nroorden")
        usuario = data.get("usuario")
        total = data.get("total")
        carrito = data.get("carrito")

        if not all([nro_orden, usuario, total, carrito]):
            return jsonify({"estado": "Error", "detalle": "Faltan datos"}), 422

        try:
            url = webpay_service.iniciar_pago(data)
            return jsonify({"estado": "ok", "redirect": url})
        except Exception as e:
            return jsonify({"estado": "Error", "detalle": str(e)}), 500



    # obtener el token de la transacción de webpay y confirmar pago
    @app.route('/confirmar_pago', methods=["GET", "POST"])
    def Confirmar_pago():
        token = request.form.get("token_ws") or request.args.get("token_ws")
        print(f"Token recibido: {token}")

        if not token:
            return jsonify({"estado": "Error", "detalle": "Token no recibido"}), 400

        try:
            response = webpay_service.confirmar_pago(token)
            status = response.get("status")

            # Redirige con la información
            return redirect(f"http://localhost:8000/pago_exitoso?estado={status}&token={token}")


        except Exception as e:
            return jsonify({"estado": "Error", "detalle": str(e)}), 500
        
    @app.route('/guardar_pago', methods=["POST"])
    def guardar_pago():
        try:
            carrito_raw = request.form.get("carrito")
            carrito = json.loads(carrito_raw) if carrito_raw else []
            usuario = request.form.get("usuario")
            total = request.form.get("total")
            estado = request.form.get("estado")
            token = request.form.get("token")
            tipo = request.form.get("tipo")

            print(carrito)
            print(usuario)
            print(total)
            print(estado)
            print(token)
            print(tipo)

            # Crear el pedido y obtener su ID
            pedido_id = pago_service.crear_pedido(total, usuario)

            # Crear detalles por cada producto en el carrito
            for producto in carrito:
                # Suponiendo que el producto tiene id, cantidad y precio (ajusta según tu estructura)
                producto_id = producto.get("id")
                cantidad = producto.get("cantidad", 1)
                precio_unitario = float(producto.get("precio", 0))
                total_producto = cantidad * precio_unitario

                pago_service.crear_detalle_pedido(pedido_id, producto_id, cantidad, total_producto)

            # Crear el registro de pago con la fecha actual
            fecha_actual = datetime.now()
            pago_service.crear_pago(pedido_id, total, fecha_actual, estado, token, tipo, usuario)

            # Redirige con la información
            return redirect(f"http://localhost:8000/resultado_pago?resultado={"exitoso"}")

        except Exception as e:
            return jsonify({"estado": "error", "detalle": str(e)}), 500
    
    
    """ Registro de Blueprints """    
    app.register_blueprint(productos)
    app.register_blueprint(externalAPIs)