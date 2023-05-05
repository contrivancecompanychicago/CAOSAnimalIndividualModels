import numpy as np
import pandas as pd
from markov import MarkovModel

# Load the Illinois Department of Public Health Mosquito Data
df_mosquito = pd.read_csv('https://www.idph.illinois.gov/DPHData/infectious-disease/mosquito-data/mosquito-data.csv')

# Load the weather data
df_weather = pd.read_csv('https://www.ncdc.noaa.gov/cdo-web/datasets/GHCND/station_id/USW00014805/data/2023/')

# Create a Regular Markov System
model = MarkovModel(df_mosquito, df_weather)

# Train the Regular Markov System on the Illinois Department of Public Health Mosquito Data and the weather data
model.fit()

# Generate new mosquito data using the Regular Markov System
new_data = model.sample(n=100)

# Print the new mosquito data
print(new_data)
