def procesar_canciones(datos, limite=10):
    """Paso 3: limpia y deja solo campos útiles."""
    if "data" not in datos:
        return []

    return [
        {
            "titulo": c["title"],
            "artista": c["artist"]["name"],
            "album": c["album"]["title"],
            "duracion_seg": c["duration"],
            "rank": c["rank"]
        }
        for c in datos["data"][:limite]
    ]
