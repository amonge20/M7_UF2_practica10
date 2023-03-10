import matplotlib.pyplot as plt
import pandas as pd
def totalPoblacioCiutat():
    # Leer archivo CSV
    df = pd.read_csv('List of cities proper by population density11.csv')

    # Obtener datos de población por ciudad
    cities = df['City']
    population = df['Population']

    # Crear gráfica de barras
    plt.bar(cities, population)

    # Agregar título y etiquetas de eje
    plt.title('Población total por ciudad')
    plt.xlabel('Ciudad')
    plt.ylabel('Población')

    # Mostrar gráfica
    plt.show()

