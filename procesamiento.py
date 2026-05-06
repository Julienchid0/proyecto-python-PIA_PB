def procesar_canciones(datos, limite=5):
    if "data" not in datos:
        return []

    return [
        {
            "titulo": c["title"],
            "artista": c["artist"]["name"],
            "album": c["album"]["title"]
        }
        for c in datos["data"][:limite]
    ]
