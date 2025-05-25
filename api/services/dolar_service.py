from flask import jsonify
from api.models.dolar import Dolar
from api.database.divisas_api import DivisasAPI

class DolarService:
    def get_dolar_today(self):
        try:
            data = DivisasAPI.get_dolar_data()
            # Obtencion de la serie más reciente con el valor del dolar
            serie = data["serie"][0]
            
            return Dolar(
                fecha= serie["fecha"],
                valor= serie["valor"]
            ).to_dict()
        except Exception as e:
            return jsonify({"Estado": "Error en la solicitud a la API de divisas", "Mensaje": str(e)})