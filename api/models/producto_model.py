class Producto:
    def __init__(self, id, nombre, descripcion, precio, imagen, stock, garantia, marca_producto, tipo_producto_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen
        self.stock = stock
        self.garantia = garantia
        self.marca_producto = marca_producto
        self.tipo_producto_id = tipo_producto_id 

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': float(self.precio),
            'imagen': self.imagen,
            'garantia': self.garantia,
            'marca_producto': self.marca_producto,
            'tipo_producto_id': self.tipo_producto_id,
        }