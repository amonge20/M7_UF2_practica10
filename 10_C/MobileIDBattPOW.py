#no me salen las capturas
from matplotlib import pyplot
from 10_C.movil import df


def MobileIDBattPOW():
    a = df['id']
    b = df['battery_power']


    pyplot.bar(a, height=b, width=0.5)
    #pyplot.legend(a , title="idMobile")
    pyplot.show()