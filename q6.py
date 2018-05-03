import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
stations = pd.read_csv('Police_Stations.csv')

# convert crime district to string and remove decimals
crimes['District'] = crimes['District'].astype(str).str[:-2]

# merge with stations
crimes_districts = crimes.merge(stations, left_on='District', right_on='DISTRICT')

# calculate x and y coordinate differences
dX = (crimes_districts['X COORDINATE'] - crimes_districts['X Coordinate'])
dY = (crimes_districts['Y COORDINATE'] - crimes_districts['Y Coordinate'])

distance_ft = (dX**2 + dY**2).apply(np.sqrt) # Pythagorean theorem
distance = distance_ft / 5280                # convert to miles
distance.hist(bins=20)
plt.savefig('crimes_by_distance.png')


