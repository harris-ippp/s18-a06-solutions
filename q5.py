import pandas as pd

# load and clean data
crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
community_populations = pd.read_csv('community_populations.csv')
socio = pd.read_csv('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
socio = socio.dropna(subset=['Community Area Number'])

# count homicides
homicides = crimes[crimes['Primary Type'] == 'HOMICIDE']
homicide_counts = homicides.groupby('Community Area').size().reset_index()
homicide_counts.columns = ['Community Area', 'Homicide Count']

# merge with populations
homicide_rates = homicide_counts.merge(community_populations,
                                       on='Community Area')

# calculate homicide rate
homicide_rates['Homicide Rate'] = (homicide_rates['Homicide Count'] /
                                   homicide_rates['Population']) * 100000

# merge with commuity area info
merged = homicide_rates.merge(socio,
                              left_on='Community Area',
                              right_on='Community Area Number')

# print highest homicide rate
highest = merged.sort_values('Homicide Rate').tail(1)
print(highest[['COMMUNITY AREA NAME', 'Homicide Rate']])

# North Lawndale has a homicide rate of 120 per 100,000 capita
