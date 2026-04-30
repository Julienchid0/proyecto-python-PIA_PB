import requests

def obtener_datos():
    """Descarga y retorna datos de JSON de la API de Deezer."""

    url = "https://api.deezer.com/search?q=soda+stereo"

    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return datos
    else:
        return {"error": "No se pudo obtener la información"}

if __name__ == "__main__":
    datos = obtener_datos()

    for cancion in datos.get("data", [])[:5]:
        print("Canción:", cancion["title"])
        print("Artista:", cancion["artist"]["name"])
        print("Álbum:", cancion["album"]["title"])
        print("-" * 30)
