from datetime import date

class PagoService:
    def __init__(self, mysql):
        self.mysql = mysql
    
    #  crear un elemento

    def crear_pedido(self, total, rut_cliente):
        cursor = self.mysql.connection.cursor()
        try:
            fecha_actual = date.today()

            # Insertar el pedido en la tabla
            cursor.execute("""
                INSERT INTO Pedido (fecha, total, cliente_id)
                VALUES (%s, %s, %s)
            """, (fecha_actual, total, rut_cliente))

            self.mysql.connection.commit()

            pedido_id = cursor.lastrowid

            # Devolver el ID del nuevo pedido
            return pedido_id
        except Exception as e:
            self.mysql.connection.rollback()
            raise e
        finally:
            cursor.close()

    def crear_detalle_pedido(self, pedido_id, producto_id, cantidad, total):
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO Detalle_Pedido (cantidad, total, pedido_id, producto_id)
                VALUES (%s, %s, %s, %s)
            """, (cantidad, total, pedido_id, producto_id))

            self.mysql.connection.commit()
        except Exception as e:
            self.mysql.connection.rollback()
            raise e
        finally:
            cursor.close()
        
    def crear_pago(self, pedido_id, total, fecha, estado, token, tipo, cliente_id):
        cursor = self.mysql.connection.cursor()
        try:
            cursor.execute("""
                INSERT INTO Pago(pedido_id, total, fecha, estado, token, tipo, cliente_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (pedido_id, total, fecha, estado, token, tipo, cliente_id))

            self.mysql.connection.commit()
        except Exception as e:
            self.mysql.connection.rollback()
            raise e
        finally:
            cursor.close()