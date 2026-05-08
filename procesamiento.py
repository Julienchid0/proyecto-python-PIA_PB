def procesar_canciones(datos, limite=10):
    if "data" not in datos:
        return []

    return [
        {
            "titulo": c["title"],
            "artista": c["artist"]["name"],
            "album": c["album"]["title"]
            "duracion_seg": c.get("duration", 0),
            "rank": c.get("rank", 0)
        }
        for c in datos["data"][:limite]
    ]
