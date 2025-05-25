from api.database.webpay_api import WebpayAPI

class WebpayService:
    def iniciar_pago(self, data):
        transaction = WebpayAPI.get_transaction()

        response = transaction.create(
            buy_order=data.get("nroorden"),
            session_id=data.get("usuario"),
            amount=data.get("total"),
            return_url="http://localhost:5000/confirmar_pago"
        )

        return response['url'] + "?token_ws=" + response['token']
    
    def confirmar_pago(self,token):
        transaction = WebpayAPI.get_transaction()
        return transaction.commit(token)