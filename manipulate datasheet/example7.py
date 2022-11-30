import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

#ncs = pd.read_csv ('ave_hi_nyc_jan_1995-2018.csv')
nyc = pd.read_csv('https://raw.githubusercontent.com/pdeitel/IntroToPython/master/examples/ch10/ave_hi_nyc_jan_1895-2018.csv')

nyc.Date = nyc.Date.floordiv(100)
nyc.columns=['Date', 'Temperature', 'Anomaly']

linear_regression= stats.linregress(x=nyc.Date,y=nyc.Temperature)
axes= sns.regplot(x=nyc.Date, y=nyc.Temperature)
#sns.set_style('whitegrid')
axes.set_ylim(5,88)
plt.title('Simple Regression using Scipy by Dr Zool')
#axes.set_xlim(2000,2022)
plt.show()
