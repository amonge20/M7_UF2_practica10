import pandas as pd
import matplotlib.pyplot as plt

def total_deaths_per_month(file, cities):
    # leemos el archivo csv
    dataframe = pd.read_csv(file)
    # seleccionamos solo los datos de las ciudades especificadas
    dataframe = dataframe[dataframe['location'].isin(cities)]
    # agrupamos los datos por ciudad y mes
    dataframe = dataframe.groupby(['location', pd.to_datetime(dataframe['date']).dt.strftime('%B')])['total_deaths'].sum().reset_index()
    # graficamos los resultados
    dataframe.pivot(index='location', columns='date', values='total_deaths').plot(kind='bar', stacked=True)
    plt.xlabel('City')
    plt.ylabel('Total Deaths')
    plt.title('Total Deaths per Month by City')
    plt.show()


