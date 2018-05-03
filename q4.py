import pandas as pd
import matplotlib.pyplot as plt

block_populations = pd.read_csv('Population_by_2010_Census_Block.csv')
tract_community = pd.read_csv('community_tracts.csv')

block_populations['CENSUS BLOCK'] = block_populations['CENSUS BLOCK'].astype(str).str.zfill(10)
block_populations['CENSUS TRACT'] = block_populations['CENSUS BLOCK'].str[:6]

tract_community['CENSUS TRACT'] = tract_community['Census Tract'].astype(str).str[-6:]

block_populations_merged = block_populations.merge(tract_community)
community_populations = block_populations_merged.groupby('Community Area')['TOTAL POPULATION'].sum()
community_populations = community_populations.reset_index()
community_populations.columns = ['Community Area', 'Population']
community_populations.to_csv('community_populations.csv', index=False)
