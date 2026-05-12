# proyecto-python-PIA_PB
Repositorio de Julien y Abi

Nancy Abigail Barrera Treviño
Julien Yabriel González García

Este API sirve para acceder a información musical, tal como Artistas, bandas, álbumes, éxitos, duración de las canciones (si es que lo solicitas).
Si buscas cualquier artista, género u álbum, te dá diferentes resultados acerca de lo que pides en cuanto a la información de la música.

Se utilizó Deezer APi https://api.deezer.com

¿Cómo ejecutarlo?
1. Hace una petición con requests.get()
2. Recibe datos en formato JSON
3. Extrae información relevante: (título de la canción, artista, álbum)
4. Usa datos para imprimir resultados y generar gráficas.

Gráfica 1: la primera gráfica cuenta canciones contiene cada álbum
Gráfica 2: Cuenta la cantidad de canciones por artista
Gráfica 3: Se tiene un conteo de la duración y reproducciones de cada canción

Este proyecto del uso del API deezer, nos permitió integrar reales dentro del programa. Aunque presenta alunas limitaciones como el filtrado por género, el cual, si intentas buscar el género, no siempre0 te aparecen los artistas más populares de ese género, sino que aparecen canciones llamadas "rock" o "pop".
Con este proyecto aprendimos a como hacer uso de un API para obtener datos reales de internet, lo cual nos ayudará en un futuro para saber trabajar con muchos más API's distintos. También aprendimos a transformar información a recursos visuales, tales son las gráficas.
