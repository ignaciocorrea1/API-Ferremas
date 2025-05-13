import requests

class DivisasAPI:
    # Base
    urlBase = "https://mindicador.cl/api/"
    
    @staticmethod
    def get_dolar_data():
        # Solicitud a la api para la informacion del dolar
        response = requests.get(DivisasAPI.urlBase + "dolar/")
        response.raise_for_status()
        return response.json()
        