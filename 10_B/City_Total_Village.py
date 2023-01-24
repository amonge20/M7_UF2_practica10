import pandas as pd
import matplotlib.pyplot as plt

#EXERCICI 1 DEL B
def City_Total_Village():
    df = pd.read_csv("List of cities proper by population density11.csv", usecols=['City', 'Population'])
    print(df(10))