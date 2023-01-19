import matplotlib.pyplot as plt
import numpy as np

def main():
    window = plt.figure()

    graf1 = number_deaths_per_month_country(2,2,1)
    graf2 = total_cases_per_month(2,2,2)
    graf3 = total_death_per_month(2,2,3)

    graf1.hist(np.randn(100), bins=20, color='b', alpha=0.3)
    graf2.scater(np.arange(30), np.arange(30) + 3*np.random.randn(30))
    graf3.plot(np.random.randn(50).cumsum(), 'k--')
    plt.show()














#