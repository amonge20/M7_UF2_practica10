#no me salen las capturas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Guardamos los datos en una variable
fitxer = pd.read_csv("test.csv")

#Guardamos los datos en un dataframe y le quitamos los datos null
df = pd.DataFrame(fitxer).dropna()

#Quitamos las comas para que no de errores al mostrar las gráfica
df = df.replace(',','', regex=True)

df = df.head(10)

colores = ["#00cc44",
           "#ff7700",
           "#ff0000",
           "#ff0099",
           "#ff0069",
           "#00cc44",
           "#ff7700",
           "#ff0000",
           "#ff0099",
           "#ff0069"
          ]