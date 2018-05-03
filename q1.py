import pandas as pd
import matplotlib.pyplot as plt

# load and clean data
crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
socio = pd.read_csv('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
socio = socio.dropna(subset=['Community Area Number'])

# calculate crimes by community area
crime_counts = crimes['Community Area'].value_counts().reset_index()
crime_counts.columns = ['Community Area', 'Crime Count']

# merge with socioeconomic data
crime_counts_socio = crime_counts.merge(socio, left_on='Community Area', right_on='Community Area Number')

# plot
crime_counts_socio.plot(kind='scatter', y='Crime Count', x='PER CAPITA INCOME ')
plt.savefig('crimes_by_income.png')
