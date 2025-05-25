class Detalle_pedido:
    def __init__(self, id, cantidad, total, pedido_id, producto_id):
        self.id = id
        self.cantidad = cantidad
        self.total = total
        self.pedido_id = pedido_id
        self.producto_id = producto_id

    def to_dict(self):
        return {
            "id": self.id,
            "cantidad": self.cantidad,
            "total": self.total,
            "pedido_id": self.pedido_id,
            "producto_id": self.producto_id,
        }