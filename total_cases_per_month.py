import pandas as pd
import matplotlib.pyplot as plt

def total_cases_per_month():
    # leemos el archivo csv
    countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Anguilla', 'Bangladesh', 'Hungary', 'Chile', 'Uruguay', 'Paraguay']
    total_cases_per_month('df_covid19_countries.csv', countries)
    # seleccionamos solo los datos de los países especificados
    dataframe = dataframe[dataframe['location'].isin(countries)]
    # agrupamos los datos por país y mes
    dataframe = dataframe.groupby(['location', pd.to_datetime(dataframe['date']).dt.strftime('%B')])['total_cases'].sum().reset_index()
    # graficamos los resultados
    dataframe.pivot(index='location', columns='date', values='total_cases').plot(kind='bar', stacked=True)
    plt.xlabel('Country')
    plt.ylabel('Total Cases')
    plt.title('Total Cases per Month by Country')
    plt.show()






