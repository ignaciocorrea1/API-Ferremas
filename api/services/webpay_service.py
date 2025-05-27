from api.database.webpay_api import WebpayAPI

# Diccionario en memoria (temporal)
carritos_temporales = {}

class WebpayService:
    def iniciar_pago(self, data):
        transaction = WebpayAPI.get_transaction()

        response = transaction.create(
            buy_order=data.get("nroorden"),
            session_id=data.get("usuario"),
            amount=data.get("total"),
            return_url="http://localhost:5000/confirmar_pago"
        )

        token = response['token']
        carrito = data.get("carrito")
        carritos_temporales[token] = carrito

        return response['url'] + "?token_ws=" + token
    
    def confirmar_pago(self,token):
        transaction = WebpayAPI.get_transaction()
        return transaction.commit(token)

    def obtener_carrito_por_token(self,token):
        return carritos_temporales.get(token)

    def eliminar_carrito_por_token(self,token):
        if token in carritos_temporales:
            del carritos_temporales[token]