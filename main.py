from api_conexion import obtener_datos
from procesamiento import procesar_canciones
from graficas import grafica_albumes, grafica_artistas

def main():
    datos = obtener_datos("soda stereo")
    canciones = procesar_canciones(datos, limite=10)

    if not canciones:
        print("No hay datos para mostrar")
        return

    grafica_albumes(canciones)
    grafica_artistas(canciones)
    grafica_duracion(canciones)

if __name__ == "__main__":
    main()
