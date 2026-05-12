import requests

def obtener_datos():
    """Descarga y retorna datos de JSON de la API de Deezer."""

    url = "https://api.deezer.com/search?q=rock"

    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return {"error": "No se pudo obtener la información"}
