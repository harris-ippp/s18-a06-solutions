import pandas as pd

crimes = pd.read_csv('Crimes_-_2001_to_present.csv')
community_populations = pd.read_csv('community_populations.csv')
socio = pd.read_csv('Census_Data_-_Selected_socioeconomic_indicators_in_Chicago__2008___2012.csv')
socio = socio.dropna(subset=['Community Area Number'])

homicide_counts = crimes[crimes['Primary Type'] == 'HOMICIDE'].groupby('Community Area').size().reset_index()
homicide_counts.columns = ['Community Area', 'Homicide Count']
homicide_rates = homicide_counts.merge(community_populations, on='Community Area')
homicide_rates['Homicide Rate'] = homicide_rates['Homicide Count'] /  homicide_rates['Population'] * 100000

merged = homicide_rates.merge(socio, left_on='Community Area', right_on='Community Area Number')

print(merged.sort_values('Homicide Rate').tail(1)[['COMMUNITY AREA NAME', 'Homicide Rate']])

# North Lawndale has a homicide rate of 120 per 100,000 capita
