# Column names of the merged World Happiness Report datasets
COUNTRY = 'Country'
YEAR = 'Year'
HAPPINESS_RANK = 'Happiness rank'
HAPPINESS_SCORE = 'Happiness score'
GDP_PER_CAPITA = 'GDP per capita'
SOCIAL_SUPPORT = 'Social support'
HEALTH = 'Life expectancy'
FREEDOM = 'Freedom'
CORRUPTION = 'Perceptions of corruption'
GENEROSITY = 'Generosity'
DYSTOPIA_RESIDUAL = 'Dystopia residual'

# Indicators which are expected to indicate urbanization if their values are high
URBANIZATION_INDICATORS = [
    'Air transport, freight (million ton-km)',
    'Air transport, passengers carried',
    'Annual freshwater withdrawals, industry (% of total freshwater withdrawal)',
    'CO2 emissions (metric tons per capita)',
    'Commercial bank branches (per 100,000 adults)',
    'Employment in industry (% of total employment) (modeled ILO estimate)',
    'Employment in services (% of total employment) (modeled ILO estimate)',
    'Industry (including construction), value added per worker (constant 2010 US$)',
    'Manufacturing, value added (% of GDP)',
    'Medium and high-tech industry (% manufacturing value added)',
    'Railways, goods transported (million ton-km)',
    'Railways, passengers carried (million passenger-km)',
    'Urban population (% of total)',
    
    # Other indicators that could be used (internet access tends to be better in densely populated areas, more universities in
    # cities)
    'Individuals using the Internet (% of population)',
    "Educational attainment, competed at least Bachelor's or equivalent, population 25+, total (%) (cumulative)",
    "Educational attainment, competed at least Master's or equivalent, population 25+, total (%) (cumulative)",
]

# Indiccators which are expected to indicate urbanization if their values are low
ANTI_URBANIZATION_INDICATORS = [
    'Agriculture, forestry, and fishing, value added per worker (constant 2010 US$)',
    'Annual freshwater withdrawals, agriculture (% of total freshwater withdrawal)',
    'Employment in agriculture (% of total employment) (modeled ILO estimate)',
    'Forest area (% of land area)',
]