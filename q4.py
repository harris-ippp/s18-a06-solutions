import pandas as pd

# load data
block_populations = pd.read_csv('Population_by_2010_Census_Block.csv')
tract_community = pd.read_csv('tract_community.csv')

# extract census tract from block_populations
block_populations['CENSUS BLOCK'] = block_populations['CENSUS BLOCK'].astype(str).str.zfill(10)
block_populations['CENSUS TRACT'] = block_populations['CENSUS BLOCK'].str[:6]

# extract census tract from tract_community
tract_community['CENSUS TRACT'] = tract_community['Census Tract'].astype(str).str[-6:]

# merge
block_populations_merged = block_populations.merge(tract_community)

# aggregate
community_populations = block_populations_merged.groupby('Community Area')['TOTAL POPULATION'].sum()

# clean up and save
community_populations = community_populations.reset_index()
community_populations.columns = ['Community Area', 'Population']
community_populations.to_csv('community_populations.csv', index=False)
