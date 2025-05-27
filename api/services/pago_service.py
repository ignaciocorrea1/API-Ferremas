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
            
    # PARCHE
    def crear_detalle_pedido_respaldo(self, pedido_id, total_pedido):
        """
        Crea un detalle de pedido usando el Taladro Bosch como producto de respaldo
        cuando el carrito está vacío debido a problemas con localStorage en WebPay
        """
        try:
            cursor = self.mysql.connection.cursor()
            
            # Primero verificar si existe el producto Taladro Bosch (debería ser el primer producto)
            cursor.execute("SELECT id FROM Producto WHERE nombre LIKE '%Taladro%Bosch%' LIMIT 1")
            producto_bosch = cursor.fetchone()
            
            if producto_bosch:
                producto_id = producto_bosch[0]
                print(f"🔧 Usando Taladro Bosch (ID: {producto_id}) como producto de respaldo")
            else:
                # Si no encuentra el Taladro Bosch, usar ID 1 como fallback
                producto_id = 1
                print(f"⚠️  Taladro Bosch no encontrado, usando producto ID: {producto_id} como respaldo")
            
            # Insertar detalle de pedido con el producto de respaldo
            query = """
            INSERT INTO Detalle_Pedido (cantidad, total, pedido_id, producto_id)
            VALUES (%s, %s, %s, %s)
            """
            
            valores = (
                1,                    # cantidad: 1 unidad
                float(total_pedido),  # total: el monto total del pedido
                pedido_id,           # pedido_id
                producto_id          # ID del Taladro Bosch o producto fallback
            )
            
            cursor.execute(query, valores)
            self.mysql.connection.commit()
            cursor.close()
            
            print(f"✅ Detalle de pedido de respaldo creado:")
            print(f"   - Pedido ID: {pedido_id}")
            print(f"   - Producto ID: {producto_id} (Taladro Bosch de respaldo)")
            print(f"   - Total: ${total_pedido}")
            
        except Exception as e:
            print(f"❌ Error creando detalle de respaldo: {str(e)}")
            raise e