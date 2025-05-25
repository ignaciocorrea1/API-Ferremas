class Usuario:
    def __init__(self, rut, dv, nombre, correo, contrasenia, direccion, telefono, tipo_usuario_id):
        self.rut = rut
        self.dv = dv
        self.nombre = nombre
        self.correo = correo
        self.contrasenia = contrasenia
        self.direccion = direccion
        self.telefono = telefono
        self.tipo_usuario_id = tipo_usuario_id 

    def to_dict(self):
        return {
            "rut": self.rut,
            "dv": self.dv,
            "nombre": self.nombre,
            "correo": self.correo,
            "contrasenia": self.contrasenia,
            "direccion": self.direccion,
            "telefono": self.telefono,
            "tipo_usuario_id": self.tipo_usuario_id,
        }