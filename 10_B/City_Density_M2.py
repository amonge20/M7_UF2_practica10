import pandas as pd
import matplotlib.pyplot as plt

#EXERCICI 3 DEL B
def City_Density_M2():
    # Leer archivo CSV
    df = pd.read_csv('List of cities proper by population density11.csv')

    # Obtener datos de densidad por ciudad
    cities = df['City']
    density = df['Density']

    # Crear gráfica de barras
    plt.bar(cities, density)

    # Agregar título y etiquetas de eje
    plt.title('Densidad de población por ciudad')
    plt.xlabel('Ciudad')
    plt.ylabel('Densidad (habitantes por m^2)')

    # Mostrar gráfica
    plt.show()


