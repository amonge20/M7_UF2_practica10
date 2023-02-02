#no me salen las capturas
from matplotlib import pyplot
from 10_C.movil import df, colores


def MobileIDSpeed():

    a = df['id']
    b = df['clock_speed']

    pyplot.bar(a, height=b, width=0.5)
    #pyplot.legend(a, title="VelocitatEnSegons/idMobil")

    pyplot.show()
