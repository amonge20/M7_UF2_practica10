from matplotlib import pyplot as plt
#### Leer archivo CSV y convertilo en un Dataframa
df = pd.read_csv('datos_covid2019.csv',index_col=None)
### Imprime el dataframe
df.head()


### Gráfica 1
fig, ax = plt.subplots()
plt.figure(figsize=(10,6))

row = df.drop('nombre',axis=1).iloc[32]
row.plot(lw=2, colormap='jet', marker='.', markersize=10,title='Contagios Confirmados COVID al día 6 de Junio',ax=ax)