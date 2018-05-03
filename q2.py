import pandas as pd
import matplotlib.pyplot as plt

# load and clean data
crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
socio = pd.read_csv('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
socio = socio.dropna(subset=['Community Area Number'])

# calculate homicides by community area
homicides = crimes[crimes['Primary Type'] == 'HOMICIDE']
homicide_counts = homicides['Community Area'].value_counts().reset_index()
homicide_counts.columns = ['Community Area', 'Homicide Count']

# right merge to retain community areas with no homicides
homicide_counts_socio = homicide_counts.merge(socio, 
                                              left_on='Community Area', 
                                              right_on='Community Area Number',
                                              how='right')
# fill missing homicide counts with zeros
homicide_counts_socio['Homicide Count'].fillna(0, inplace=True)

# plot
homicide_counts_socio.plot(kind='scatter', y='Homicide Count', x='PER CAPITA INCOME ')
plt.savefig('homicides_by_income.png')
