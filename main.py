from api_deezer import obtener_datos
from procesamiento import procesar_canciones
from graficas import grafica_albumes, grafica_artistas, grafica_duracion


def main():

    print("Obteniendo datos de Deezer...")

    datos = obtener_datos()

    print("Procesando canciones...")

    canciones = procesar_canciones(datos, limite=10)

    if not canciones:
        print("No hay datos para mostrar")
        return

    print("\nCanciones encontradas:\n")

    for c in canciones:
        print(f"{c['titulo']} - {c['artista']}")

    print("\nGenerando gráficas...")

    grafica_albumes(canciones)
    grafica_artistas(canciones)
    grafica_duracion(canciones)

    print("Proceso terminado")


if __name__ == "__main__":
    main()
