import matplotlib.pyplot as plt
from collections import Counter


# GRÁFICA 1: Cantidad de canciones por album
def grafica_albumes(canciones):
    albumes = [c["album"] for c in canciones]   #Extraemos el nombre del albúm de cada canción
    conteo = Counter(albumes)   #Contamos cuantas veces se repite
    nombres = list(conteo.keys())   #Preparamos los datos para los ejes: x(nombres), y(cantidades)
    cantidades = list(conteo.values())

    plt.figure(figsize=(10, 5))   #Definimos el tamaño de la ventana de la gráfica
    plt.bar(nombres, cantidades, color="skyblue")   #Creamos una gráfica de barras de color azul claro
 #Añadimos titulos y etiquetas 
    plt.title("Canciones por álbum")   
    plt.xlabel("Álbum")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)   #Rotamos los nombres de los albumes para que no se amontonen
 #Ajustamos el diseño auomatico y guardamos como imagen
    plt.tight_layout()   
    plt.savefig("grafica1.png")   
    plt.show()


# GRÁFICA 2: Distribucion de canciones por artista
def grafica_artistas(canciones):
    artistas = [c["artista"] for c in canciones]   #Obtenemos la lista de todos los artistas
    conteo = Counter(artistas)   #Contamos cuantas canciones tiene cada artista
 #Preparamos los datos para los ejes: x(nombres), y(cantidades) 
    nombres = list(conteo.keys())  
    cantidades = list(conteo.values())

    plt.figure(figsize=(8, 8)) #Configuramos una figura cuadrada para el gráfico de pastel
 #Creamos el gráfico de pastel con etiquetas y porcentajes
    plt.pie(
        cantidades,
        labels=nombres,
        autopct="%1.1f%%"
    )  
    plt.title("Distribución de artistas")   #Añadimos un titulo 
 #Guardamos y mostramos el resultado 
    plt.savefig("grafica2.png")
    plt.show()


# GRÁFICA 3: Gráfica de duración vs reproducciones
def grafica_duracion(canciones):
   #Extraeos la duración en segundos y las reproducciones de cada canción
    duraciones = [c["duracion_seg"] for c in canciones]   
    reproducciones = [c["rank"] for c in canciones]

    plt.figure(figsize=(10, 6))   #Configuramos el tamaño del gráfico
 #Creamos el grafico de color morado
 #alpha=0.5 hace que los puntos sean semitransparentes para ver si se enciman
    plt.scatter(duraciones, reproducciones, alpha=0.5, color="purple")   

 #Añadimos un titulo y etiquetas
    plt.title("Relación: Duración vs Reproducciones")  
    plt.xlabel("Duración (segundos)")
    plt.ylabel("Rank")
    plt.grid(True)  #Activamos la cuadricula de fondo para facilitar la lectura de los puntos               
  #Guardamos y mostramos el resultado  
    plt.savefig("grafica3.png")      
    plt.show()
