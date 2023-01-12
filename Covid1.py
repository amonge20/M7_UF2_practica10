import pandas as pd

def Covid1(dades):
    dades = pd.read_csv('df_covid19_countries.csv')
    print (dades.head(10))