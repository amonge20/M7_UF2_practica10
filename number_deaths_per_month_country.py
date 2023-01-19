from matplotlib import pyplot as plt
def deaths_per_month_by_country(data, countries):
    """
    Mostra el número de morts per mes per país
    :param data: DataFrame amb les dades
    :param countries: Llista de països a mostrar
    """
    data = data[data['Country'].isin(countries)]
    data = data.groupby(['Country', 'Month']).sum()['Deaths'].reset_index()
    data = data.pivot(index='Month', columns='Country', values='Deaths')
    data.plot(kind='line', legend=True)
    plt.show()
    plt.plot(lw=2, colormap='jet', marker='.', markersize=10,title='Contagios Confirmados COVID al día 6 de Junio',ax=ax)