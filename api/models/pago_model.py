class Pago:
    def __init__(self, id, pedido_id, total, fecha, estado, token, tipo, rut):
        self.id = id
        self.pedido_id = pedido_id
        self.total = total
        self.fecha = fecha
        self.estado = estado
        self.token = token
        self.tipo = tipo
        self.rut = rut

    def to_dict(self):
        return {
            "id": self.id,
            "pedido_id": self.pedido_id,
            "total": self.total,
            "fecha": self.fecha,
            "estado": self.estado,
            "token": self.token,
            "tipo": self.tipo,
            "rut": self.rut,
        }