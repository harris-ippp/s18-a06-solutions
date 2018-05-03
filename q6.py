import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
stations = pd.read_csv('Police_Stations.csv')

crimes['District'] = crimes['District'].astype(str).str[:-2]
crimes_districts = crimes.merge(stations, left_on='District', right_on='DISTRICT')

dX = (crimes_districts['X COORDINATE'] - crimes_districts['X Coordinate'])
dY = (crimes_districts['Y COORDINATE'] - crimes_districts['Y Coordinate'])

distance = (dX**2 + dY**2).apply(np.sqrt) / 5280
distance.hist(bins=20)
plt.savefig('crimes_by_distance.png')


