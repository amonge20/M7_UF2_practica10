#no me salen las capturas
from matplotlib import pyplot
from 10_C.movil import df


def MobileIDMegapixels():

    a = df['id']
    b = (df['px_height'] * df['px_width'])/1000000

    pyplot.bar(a, height=b, width=0.5)
    # pyplot.legend(a, title="Megapíxels/idMobil")
    pyplot.show()

