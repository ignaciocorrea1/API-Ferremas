from api.models.producto_model import Producto

class ProductoService:
    def __init__(self, mysql):
        self.mysql = mysql
        
    # GET todos los productos de la BD
    def get_productos(self):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM producto")
        resultado = cursor.fetchall() # Resultado es una tupla con tuplas dentro
        cursor.close()
        
        # Convertir a diccionarios las tuplas a traves de list comprehension
        productos = [
            Producto(
                id=fila[0],
                nombre=fila[1],
                descripcion=fila[2],
                precio=fila[3],
                imagen=fila[4],
                stock=fila[5],
                garantia=fila[6],
                marca_producto=fila[7],
                tipo_producto_id=fila[8]
                ).to_dict() for fila in resultado
        ]
        
        # Retorna la lista de los productos
        return productos
    
    #  GET un producto por id
    def get_producto_by_id(self, id):
        cursor = self.mysql.connection.cursor()
        cursor.execute("SELECT * FROM producto WHERE id = %s", (id,))
        resultado = cursor.fetchone()
        cursor.close()
        
        if resultado:
            producto = Producto(
                id=resultado[0],
                nombre=resultado[1],
                descripcion=resultado[2],
                precio=resultado[3],
                imagen=resultado[4],
                stock=resultado[5],
                garantia=resultado[6],
                marca_producto=resultado[7],
                tipo_producto_id=resultado[8]
            )
            return producto.to_dict()
        return None