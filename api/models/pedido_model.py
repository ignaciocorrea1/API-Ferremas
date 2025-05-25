class Pedido:
    def __init__(self, id, fecha, total, rut):
        self.id = id
        self.fecha = fecha
        self.total = total
        self.rut = rut 

    def to_dict(self):
        return {
            "id": self.id,
            "fecha": self.fecha,
            "total": self.total,
            "rut": self.rut,
        }