import pandas as pd
import matplotlib.pyplot as plt

# load data
crimes = pd.read_csv('Crimes_-_2001_to_present.csv')

# extract hour from each crime datetime
crimes['Hour'] = pd.to_datetime(crimes.Date).dt.hour

# mean of a boolean is proportion
domestic_prop = crimes.groupby('Hour')['Domestic'].mean()

# plot
domestic_prop.plot()
plt.savefig('domestic_prop.png')
