import pandas as pd
import matplotlib.pyplot as plt

crimes = pd.read_csv('Crimes_-_2001_to_present.csv')

crimes['Hour'] = pd.to_datetime(crimes.Date).dt.hour
domestic_prop = crimes.groupby('Hour')['Domestic'].mean()
domestic_prop.plot()
plt.savefig('domestic_prop.png')
