import matplotlib.pyplot as plt
from collections import Counter


# GRÁFICA 1: BARRAS
def grafica_albumes(canciones):
    albumes = [c["album"] for c in canciones]
    conteo = Counter(albumes)
    nombres = list(conteo.keys())
    cantidades = list(conteo.values())

    plt.figure(figsize=(10, 5))
    plt.bar(nombres, cantidades, color="skyblue")
    plt.title("Canciones por álbum")
    plt.xlabel("Álbum")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("grafica1.png")
    plt.show()


# GRÁFICA 2: PASTEL
def grafica_artistas(canciones):
    artistas = [c["artista"] for c in canciones]
    conteo = Counter(artistas)
    nombres = list(conteo.keys())
    cantidades = list(conteo.values())

    plt.figure(figsize=(8, 8))
    plt.pie(
        cantidades,
        labels=nombres,
        autopct="%1.1f%%"
    )
    plt.title("Distribución de artistas")
    plt.savefig("grafica2.png")
    plt.show()


# GRÁFICA 3: 
def grafica_duracion(canciones):
    duraciones = [c["duracion_seg"] for c in canciones]
    reproducciones = [c["rank"] for c in canciones]

    plt.figure(figsize=(10, 6))
    plt.scatter(duraciones, reproducciones, alpha=0.5, color="purple")
    
    plt.title("Relación: Duración vs Reproducciones")
    plt.xlabel("Duración (segundos)")
    plt.ylabel("Rank")
    plt.grid(True) # Ayuda a leer mejor los puntos
    plt.savefig("grafica3.png")
    plt.show()
